"""O231 §6: forced/unforced split for SQ_± (signed words, t u v != 0) with |t| <= T at given n = 1 (8).
Sides |tn+1|, |n+u|, |n+v| (a zero side counts as clean); clean = no prime factor r with Jacobi (r/n) = -1.
chi = (-A/n) = (A/n) (Jacobi; n = 1 (4)).  Reports: words W, certificates Nm, unforced U, forced fraction, and the least
|t| of a certificate / of an unforced word.  usage: [STRICT=1] z7_sqpm_split.py T n1 n2 ..."""
import sys, os
STRICT = bool(os.environ.get('STRICT'))  # exclude positive words (strictly signed version)
from sympy import factorint, jacobi_symbol as J
T = int(sys.argv[1])
def jac(a, n): return J(a % n, n)
for n in map(int, sys.argv[2:]):
    cache = {}
    def clean(x):
        x = abs(x)
        if x == 0: return True
        if x not in cache: cache[x] = all(jac(r, n) != -1 for r in factorint(x))
        return cache[x]
    W = Nm = U = 0; tc = tu = None
    for at in range(1, T + 1):
        for t in (at, -at):
            N = t * n + 1; f = factorint(abs(N)); ds = [1]
            for r, e in f.items(): ds = [d * r ** k for d in ds for k in range(e + 1)]
            for d in ds:
                for A in (d, -d):
                    if (A + 1) % t: continue
                    B = N // A
                    if (B + 1) % t: continue
                    u, v = (A + 1) // t, (B + 1) // t
                    if u == 0 or v == 0: continue
                    if STRICT and t > 0 and u > 0 and v > 0: continue
                    W += 1; c = jac(A, n) == -1; Nm += c
                    unf = not clean(N) and not clean(n + u) and not clean(n + v); U += unf
                    if c and tc is None: tc = at
                    if unf and tu is None: tu = at
    print(f"n={n} |t|<={T}: W={W} Nm={Nm} U={U} forced={1 - U / W:.3f} Nm/U={Nm / max(U, 1):.3f} least|t| cert={tc} unforced={tu}")
