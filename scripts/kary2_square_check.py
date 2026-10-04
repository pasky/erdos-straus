"""KARY2 Lemmas 2.1(2), 2.2: (a,D)- and Case-A classes contain no square mod G.

Brute force: a residue c is a square mod G iff it is a square mod every
p^e || G (CRT); squares mod p^e are enumerated and cached.
Usage: python kary2_square_check.py [AMAX DMAX DAMAX]
"""
import sys
from functools import lru_cache
from sympy import factorint, divisors

@lru_cache(maxsize=None)
def squares(q):
    return frozenset((x * x) % q for x in range(q))

def is_square_mod(c, G):
    for p, e in factorint(G).items():
        q = p ** e
        if c % q not in squares(q):
            return False
    return True

def g_of(D):
    g = 1
    for p, e in factorint(D).items():
        g *= p ** ((e + 1) // 2)
    return g

def main():
    AMAX, DMAX, DAMAX = (int(x) for x in sys.argv[1:4]) if len(sys.argv) > 3 else (60, 600, 6000)
    bad = 0; n = 0
    for a in range(1, AMAX + 1):
        for D in range(1, DMAX + 1):
            G = 4 * a * g_of(D)
            c = (-(4 * D + a)) % G
            n += 1
            if is_square_mod(c, G):
                bad += 1; print("aD square:", a, D, G, c)
    print(f"(a,D): a<={AMAX}, D<={DMAX}: {n} classes, {bad} contain a square mod G")
    assert bad == 0
    # control: the shifted residues c+1 are often squares (tests is_square_mod)
    ctrl = sum(is_square_mod((-(4 * D + a) + 1) % (4 * a * g_of(D)), 4 * a * g_of(D))
               for a in range(1, 21) for D in range(1, 101))
    print(f"control: {ctrl} of 2000 shifted residues c+1 are squares mod G")
    assert ctrl > 0
    bad = 0; n = 0
    for d in range(1, DAMAX + 1):
        g = g_of(d); G = 4 * g
        for m in divisors(4 * d + 1):
            c = (-pow(m, -1, G)) % G
            n += 1
            if is_square_mod(c, G):
                bad += 1; print("CaseA square:", d, m, G, c)
    print(f"Case A: d<={DAMAX}: {n} classes, {bad} contain a square mod G")
    assert bad == 0

if __name__ == "__main__":
    main()
