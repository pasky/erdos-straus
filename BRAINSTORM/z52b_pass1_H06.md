# z52b Pass 1 — batch H06

(summary to be filled in when the batch is complete)

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
