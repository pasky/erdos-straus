"""review_fz_q9.py (R220, from scratch): exact Case B tuple counts over F_9 for small s (same enumeration as
review_fz_brute.py: v1, then ordered factorisations of T^{s-2} + v1), and the exact union-bound contribution
sum_s count(s) q^{1 - ceil(s/2)} (all tuples, both orders of (w, C)), to compare with the route-bound sum of §4
(Σ_{s<=8} = 9.22 with the bounds).  usage: uv run --with python-flint python scripts/review_fz_q9.py SMAX"""
import sys
from itertools import product
from fractions import Fraction
import flint

SMAX = int(sys.argv[1])
F9 = flint.fq_default_ctx(3, 2)
R = flint.fq_default_poly_ctx(F9)
z = F9.gen()
ELTS = [F9(a) + F9(b) * z for a in range(3) for b in range(3)]
NZ = [x for x in ELTS if x != 0]
T = R([0, 1]); one = R([1])
q = 9


def divisors(F):
    c, fac = F.factor()
    divs = [one]
    for (g, k) in fac:
        divs = [d * g**i for d in divs for i in range(k + 1)]
    return divs


def ismonic(f):
    return f.degree() >= 0 and f.leading_coefficient() == 1


tot = Fraction(0)
for s in range(3, SMAX + 1):
    Ts2 = T**(s - 2)
    n = 0
    for e in range(0, s - 2):
        for low in product(ELTS, repeat=e):
            if e > 0 and low[0] == 0:
                continue
            for lc in (F9(1), F9(2)):
                c = list(low) + [lc]
                if c[0] == 0:
                    continue
                v1 = R(c)
                F = Ts2 + v1
                Tv1 = T * v1
                for w1 in divisors(F):
                    G = F // w1
                    for C1 in divisors(G):
                        g, rem = divmod(w1 + C1, Tv1)
                        if rem != 0 or not ismonic(g) or g(F9(0)) == 0:
                            continue
                        n += 1
    tot += Fraction(n, q**((s + 1) // 2 - 1))
    print(f"q=9 s={s}: exact tuples={n}  mass={n / q**((s + 1) // 2 - 1):.6f}  cumulative={float(tot):.6f}", flush=True)
