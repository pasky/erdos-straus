"""Z0326: explicit polynomial whose positive values (over all integer inputs) are exactly {n : ES(n)}.
P = (1 + d1^2+..+d4^2) * (1 - D^2),  D = 4xyz - n(xy+yz+zx),  n = 1 + sum d_i^2, x = 1 + sum a_i^2, y = 1 + sum b_i^2,
z = 1 + sum c_i^2 (Lagrange: x,y,z,n range over all positive integers). P > 0 iff D = 0, and then P = n.
Checks: (1) degree / variable count via sympy; (2) brute force: the set of positive values of P with x,y,z <= 3n bound
equals {2 <= n <= NMAX : ES(n)} computed by the Delta_0 bounded search x <= 3n/4 (BL Lemma 3.10)."""
import json, sys
from sympy import symbols, expand, Poly
from fractions import Fraction
d = symbols('d1:5'); a = symbols('a1:5'); b = symbols('b1:5'); c = symbols('c1:5')
n = 1 + sum(t**2 for t in d); x = 1 + sum(t**2 for t in a); y = 1 + sum(t**2 for t in b); z = 1 + sum(t**2 for t in c)
D = 4*x*y*z - n*(x*y + y*z + z*x)
P = Poly(expand(n*(1 - D**2)), *(d + a + b + c))
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
def es_bounded(m):  # Delta_0: x<=y<=z, m/4 < x <= 3m/4, y <= 2mx/(4x-m), z determined
    for X in range(m // 4 + 1, 3 * m // 4 + 1):
        r = Fraction(4, m) - Fraction(1, X)
        if r <= 0: continue
        for Y in range(max(X, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fraction(1, Y)
            if s > 0 and s.numerator == 1 and s.denominator >= Y: return True
    return False
good = [m for m in range(2, NMAX + 1) if es_bounded(m)]
vals = set()
for m in range(2, NMAX + 1):  # P = m > 0 iff some x,y,z >= 1 with D = 0; search x<=y<=z directly on D
    found = False
    for X in range(1, m + 1):
        if found: break
        for Y in range(X, 2 * m * m + 2):
            num = m * X * Y; den = 4 * X * Y - m * (X + Y)
            if den <= 0:
                continue
            if num % den == 0 and num // den >= Y: vals.add(m); found = True; break
            if Fraction(num, den) < Y: break
print(json.dumps({'poly_vars': len(P.gens), 'poly_total_degree': P.total_degree(), 'poly_terms': len(P.terms()),
                  'NMAX': NMAX, 'ES_bounded_failures_2..NMAX': [m for m in range(2, NMAX + 1) if m not in good],
                  'positive_values_equal_ES_good': sorted(vals) == good}))
