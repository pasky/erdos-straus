"""EXCEPTIONAL_TWIN Remark S1 check: do (a,D)-classes -(4D+a) mod 4a*g(D)
(ET Lemma 3.2) and Case-A classes -m^{-1} mod 4g(d), m | 4d+1 (ET §3),
ever contain an integer square (unit or not) modulo their modulus?
Usage: uv run python scripts/twin_square_base_check.py amax Dmax dmax"""
import sys
from math import gcd
from sympy import factorint, divisors


def g(D):
    r = 1
    for p, e in factorint(D).items():
        r *= p ** ((e + 1) // 2)
    return r


def has_square(r, G):
    r %= G
    return any((x * x - r) % G == 0 for x in range(G))


amax, Dmax, dmax = (int(x) for x in sys.argv[1:4])
bad = n = 0
for a in range(1, amax + 1):
    for D in range(1, Dmax + 1):
        G = 4 * a * g(D)
        n += 1
        if has_square(-(4 * D + a), G):
            bad += 1
            print("aD square", a, D, G)
print(f"(a,D) classes: {n} checked (a<={amax}, D<={Dmax}, all), {bad} contain a square")
nA = badA = 0
for d in range(1, dmax + 1):
    G = 4 * g(d)
    for m in divisors(4 * d + 1):
        if gcd(m, G) != 1:
            continue
        nA += 1
        if has_square(-pow(m, -1, G), G):
            badA += 1
            print("A square", d, m, G)
print(f"Case-A classes: {nA} checked (d<={dmax}), {badA} contain a square")
sys.exit(1 if bad or badA else 0)
