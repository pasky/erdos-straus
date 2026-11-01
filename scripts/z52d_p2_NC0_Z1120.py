"""Z1120: termination orders for identity search (G4, NC0).
Setting: solutions (n; x<=y<=z) of 4/n = 1/x+1/y+1/z, n <= NMAX, enumerated exactly.
Rewrite rules tested:
  R1 gcd-descent: if g=gcd(n,x,y,z)>1 then (n;x,y,z) -> (n/g; x/g, y/g, z/g)   [still a solution]
  R2 Vieta-type jump: replace one denominator by the other root of the cleared equation in that variable.
     Cleared form: 4xyz = n(xy+yz+zx). Premise check: is it quadratic in any single variable?
  R3 sort (x,y,z) -> sorted order (permutation move).
Candidate lex measures: (n, max denominator), (n, sum of denominators), (max den, n).
Check: each rule's move strictly decreases the measure on every instance (exact, all solutions)."""
import sys, math
from fractions import Fraction

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300

# --- premise check: degree in each variable of the cleared equation F = 4xyz - n(xy+yz+zx)
import sympy as _sp  # only for the symbolic degree check
X, Y, Z, N = _sp.symbols("x y z n")
F = 4 * X * Y * Z - N * (X * Y + Y * Z + Z * X)
for v in (X, Y, Z):
    print(f"degree of F in {v}: {_sp.degree(F, v)}")
print("F(x) = x*(4yz - n(y+z)) - n*y*z  -> linear in x; the other root is never a second solution.")

sols = []
for n in range(2, NMAX + 1):
    for x in range(math.ceil(n / 4), 3 * n // 4 + 2):
        r = Fraction(4, n) - Fraction(1, x)
        if r <= 0:
            continue
        # y in [x, 2/r]
        ymax = math.floor(2 / r)
        for y in range(x, ymax + 1):
            r2 = r - Fraction(1, y)
            if r2 <= 0:
                continue
            if r2.numerator == 1:
                sols.append((n, x, y, r2.denominator))
print("solutions (n;x<=y<=z) with n<=%d: %d" % (NMAX, len(sols)))

def verify(n, x, y, z):
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

assert all(verify(*s) for s in sols)

# R1 gcd descent: measure check
r1_moves = 0; bad = {"n": 0, "maxden": 0, "sum": 0}
for (n, x, y, z) in sols:
    g = math.gcd(math.gcd(n, x), math.gcd(y, z))
    if g > 1:
        r1_moves += 1
        n2, x2, y2, z2 = n // g, x // g, y // g, z // g
        assert verify(n2, x2, y2, z2) and n2 * g == n
        if not (n2 < n): bad["n"] += 1
        if not (max(x2, y2, z2) < max(x, y, z)): bad["maxden"] += 1
        if not (x2 + y2 + z2 < x + y + z): bad["sum"] += 1
print(f"R1 moves (g>1): {r1_moves} of {len(sols)}; non-decrease counts: {bad}")

# R2 Vieta-type jump: for (n,y,z) fixed, the x-root set of the cleared equation
r2_nontrivial = 0
for (n, x, y, z) in sols:
    den = 4 * y * z - n * (y + z)
    if den == 0:
        continue
    num = n * y * z
    roots = set()
    if num % den == 0 and num // den > 0:
        roots.add(num // den)
    # other root (if any) of the linear equation is the same unique root
    roots.discard(x)
    if roots:
        r2_nontrivial += 1
print(f"R2 jumps to a different admissible x (fixed n,y,z): {r2_nontrivial} of {len(sols)}")

# lex measure report for R1 and R3 combined: (n, max den) strictly decreasing on R1 moves
print("R3 sort: permutation move; orbit size fixed by the multiset, measure-neutral (no termination content).")
print("Conclusion: only R1 (n decreases) is a non-trivial well-founded step; R2 has no non-trivial moves.")
