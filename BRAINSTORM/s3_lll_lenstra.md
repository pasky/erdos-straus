# s3_lll_lenstra — (J)25 certificate cube × (J)38 Machin lines × Lenstra/Coppersmith "divisors in residue classes"

**Combines:** (J)25 (cube (c,d,j), O(p²) box), (J)38 Prop 5.1 (line (d,j): (4cdj − 1)(4sdj − 1) = 4dj²p + 1), and the
geometry-of-numbers theorem on divisors in residue classes (brief: "LLL in the O(p²) box").

## Idea
On the (d,j)-line a certificate is a divisor of N = 4dj²p + 1 in the class −1 mod s = 4dj. Lenstra (1984): if
s > N^{1/3} there are at most 11 divisors of N in a class r mod s (gcd(r, s) = 1), all found in polynomial time;
Coppersmith–Howgrave-Graham–Nagaraj (2008): the same constructively for s > N^{1/4+ε} (count polynomial in 1/ε).
Can LLL be turned from an algorithm into an existence mechanism on the lines where it applies?

## Literature
H. W. Lenstra Jr., *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340. D. Coppersmith, N. Howgrave-Graham,
S. V. Nagaraj, *Divisors in residue classes, constructively*, Math. Comp. 77 (2008) 531–545. (Cited from memory;
statements are the standard ones, not re-checked against the PDFs.)

## Barrier screen
Lenstra regime on the line ⟺ (4dj)³ > 4dj²p + 1 ⟺ (essentially) 16d²j > p. These results are UPPER bounds (≤ 11 per
line) and decision procedures; they give no lower bound, so as existence tools they are B3/B6-blind: the lines are
independent Bernoulli trials as far as LLL knows. A short vector of the Coppersmith lattice always exists (Minkowski),
but it yields a polynomial whose small root may not exist; existence would need the root, i.e. the divisor (B2).

## Cheap numerics (`scripts/s3_lenstra_regime.py 3000`, < 1 s; all Type II cube points, primes < 3000)
Certificate pairs {h, h*}: 5465 on Lenstra-regime lines (58%), 2651 Coppersmith-only (28%), 1314 below N^{1/4} (14%).
Max pairs on a single Lenstra-regime line: **1**. Some primes have no certificate below the Coppersmith regime at all.

## Assessment
PROVED (relative to Lenstra): f_II(p) ≤ 11·#{Lenstra lines} + (rest), and the whole O(p²) box is decidable in Õ(p)
line-by-line (no better than trivial search). The certificates mostly sit where LLL sees them one at a time; LLL turns
the box into ≈ p log p independent coin flips, which is the lottery picture. No existence mechanism. Promise 0.
