"""R177 from-scratch checks of LDP_DEEP §B.0-B.1 (bsD_genus_vacuity_LDp).

For every Type II tuple (a,b,c,d) of n (4abcd - a - b = c n, i.e. f = Ma-1, f' = Mb-1, ff' = 1 + 4c^2 d n, M = 4cd):
 (B.0) e = (a+b)/c integral; Gram of (x, w = x+y) for T = [[f,1],[1,f']] is [[Ma-1, Ma],[Ma, Mce]], det = Mcn,
       = diag(-1, 0) mod M;  (also the ES solution 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn) is checked)
 (B.1) Diff(T) := finite ramification of B_T = (-f, -det T)_Q  equals {n} for n = p prime (and is odd-sized, = the
       set of l | n with odd ... for composite odd n it is printed for information).
Hilbert symbols implemented from scratch (Serre, A Course in Arithmetic, III.1.2).
Run: PYTHONPATH=scripts uv run python scripts/review_ld_gram.py X
"""
import sys
from fractions import Fraction
from sympy import factorint, primerange, isprime

X = int(sys.argv[1])


def split(a, l):
    v = 0
    while a % l == 0: a //= l; v += 1
    return v, a


def leg(u, l):
    r = pow(u % l, (l - 1) // 2, l)
    return -1 if r == l - 1 else 1


def hilbert(a, b, l):
    if l == 'inf': return -1 if a < 0 and b < 0 else 1
    al, u = split(a, l); be, w = split(b, l)
    if l != 2:
        s = (-1) ** (al * be * ((l - 1) // 2))
        return s * leg(u, l) ** be * leg(w, l) ** al
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    return (-1) ** ((eps(u) * eps(w) + al * om(w) + be * om(u)) % 2)


def diff(f, D):
    a, b = -f, -D
    ls = set(factorint(abs(a))) | set(factorint(abs(b))) | {2}
    ram = sorted(l for l in ls if hilbert(a, b, l) == -1)
    assert hilbert(a, b, 'inf') == -1 and len(ram) % 2 == 1  # Hilbert reciprocity sanity
    return ram


def tuples(n, cdmax):
    for cd in range(1, cdmax + 1):
        for c in range(1, cd + 1):
            if cd % c: continue
            d = cd // c; M = 4 * cd; N = 1 + 4 * c * c * d * n
            ds = [1]
            for l, v in factorint(N).items():
                ds = [x * l ** k for x in ds for k in range(v + 1)]
            for f in ds:
                fp = N // f
                if f <= fp and (f + 1) % M == 0 and (fp + 1) % M == 0:
                    yield c, d, (f + 1) // M, (fp + 1) // M, f, fp, M


cnt = bad = 0; comp = {}
for n in range(3, X, 2):
    for c, d, a, b, f, fp, M in tuples(n, 12):
        cnt += 1
        assert 4 * a * b * c * d - a - b == c * n
        assert Fraction(4, n) == Fraction(1, a * b * d) + Fraction(1, a * c * d * n) + Fraction(1, b * c * d * n)
        assert (a + b) % c == 0; e = (a + b) // c
        G = [[f, f + 1], [f + 1, f + 2 + fp]]  # Gram of (x, x+y) when <x,x>=f, <x,y>=1, <y,y>=f'
        ok = G == [[M * a - 1, M * a], [M * a, M * c * e]] and G[0][0] * G[1][1] - G[0][1] ** 2 == M * c * n
        ok &= [[v % M for v in r] for r in G] == [[M - 1, 0], [0, 0]]
        D = f * fp - 1
        dset = diff(f, D)
        if isprime(n):
            ok &= dset == [n]
        else:
            comp.setdefault(n, set()).add(tuple(dset))
        bad += not ok
print('Type II tuples (cd <= 12, odd n <', X, '):', cnt, ' failures:', bad)
print('composite odd n: Diff sets seen (n -> sets), first 12:', list(comp.items())[:12])
print('all Diff sets for composite n are subsets of primes dividing n:',
      all(set(s) <= set(factorint(n)) for n, ss in comp.items() for s in ss))
