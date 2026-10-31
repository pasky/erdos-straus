"""U01 Z0138 and Z0309 with a common 4-term engine.
Z0138: for n<=NMAX, min over 4-term reps n-stuff: 4/n = 1/x+1/y+1/z+1/w (x<=y<=z<=w) of w/n (least C with max denom <= C n).
Z0309: 16/n as a sum of 4 unit fractions: existence for n<=NMAX (uses 4 terms with numerator 16)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 120
def two_term_all(A, B):
    out = []
    if A <= 0: return out
    g = math.gcd(A, B); A //= g; B //= g
    # divisors of B^2 by trial factorisation of B
    f = {}; n = B; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    ds = [1]
    for q, e in f.items(): ds = [dd*q**k for dd in ds for k in range(2*e+1)]
    for dd in ds:
        if (dd + B) % A == 0:
            a = (dd+B)//A; e2 = B*B//dd
            if (e2+B) % A == 0:
                b = (e2+B)//A
                if 0 < a <= b: out.append((a, b))
    return out
def four_term(m, n, want_min_w=False, distinct=False):
    best = None; found = False
    for x in range(max(1, -(-n*1//m)), n*4+1):  # x>= n/m, x <= 4n/m? keep broad
        r1 = Fr(m, n) - Fr(1, x)
        if r1 <= 0: continue
        if x*4 < n*1 and False: continue
        for y in range(x+1 if distinct else x, 4*n+1):
            r2 = r1 - Fr(1, y)
            if r2 <= 0: continue
            if r2.numerator > 10**12: continue
            for z, w in two_term_all(r2.numerator, r2.denominator):
                if z >= y and (not distinct or (z > y and w > z)):
                    found = True
                    if best is None or w < best: best = w
            if found and not want_min_w: return True
    return best if want_min_w else found
if __name__ == "__main__":
    # Z0309: 16/n as 4 unit fractions, n<=NMAX; list exceptions
    exc16 = [n for n in range(2, NMAX+1) if not four_term(16, n, distinct=True)]
    print(f"Z0309 (distinct denominators): 16/n has no 4-term unit-fraction rep for n<={NMAX}; exceptions: {exc16[:30]}")
    # Z0138: least C with 4/n = 4 unit fractions and max denominator <= C n (n<=NMAX)
    Cs = []
    for n in range(2, NMAX+1):
        w = four_term(4, n, want_min_w=True, distinct=True)
        if w is not None: Cs.append((w/n, n))
    print(f"Z0138: n<= {NMAX}: min over n of ratio (w/n) = {min(Cs)}, max over n of least-ratio = {max(Cs)}; median = {sorted(Cs)[len(Cs)//2]}")
    print("  largest least-ratio (C_n = min_w/n) for n:", sorted(Cs, reverse=True)[:5])
