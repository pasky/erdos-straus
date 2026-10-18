"""O273 item (2): sanity check of the L^1 Fourier certificate at windows q = 3 (mod 8) (EVIDENCE only).

For primes p = 1 (mod 8) and primes q = 3 (mod 8), K = (p+q)/4 (odd), primes l | K:
  cert(p,q) := sum_{chi != 1 mod q} prod_{l | K} |1 + chi(l) + conj chi(l)| / 3  < 1.
Checks: cert => a signed squarefree product u/v = -1 (mod q) with uv | K exists, and the
explicit Type II solution 4/p = 1/K + 1/y + 1/z, y = p(K/u)(u+v)/q, z = p(K/v)(u+v)/q, holds exactly.
Also records how often cert holds at forced ((q/p) = -1) and unforced windows.
"""
import cmath
import math
import sys
from fractions import Fraction
from itertools import product

from sympy import factorint, primerange, primitive_root, legendre_symbol


def cert_value(K, q):
    g = primitive_root(q)
    dlog = {}
    x = 1
    for e in range(q - 1):
        dlog[x] = e
        x = x * g % q
    ls = [dlog[l % q] for l in factorint(K)]
    tot = 0.0
    for j in range(1, q - 1):  # characters chi_j(g) = e(j/(q-1))
        prod = 1.0
        for e in ls:
            th = 2 * math.pi * j * e / (q - 1)
            prod *= abs(1 + 2 * math.cos(th)) / 3
        tot += prod
    return tot


def witness(K, q):
    P = list(factorint(K))
    for eps in product((-1, 0, 1), repeat=len(P)):
        u = v = 1
        for l, e in zip(P, eps):
            if e == 1:
                u *= l
            elif e == -1:
                v *= l
        if (u + v) % q == 0:
            return u, v
    return None


def main(lo, hi, qmax):
    stats = {"forced": [0, 0, 0], "unforced": [0, 0, 0]}  # [windows, cert, witness]
    viol = 0
    for p in primerange(lo, hi):
        if p % 8 != 1:
            continue
        for q in primerange(3, qmax):
            if q % 8 != 3:
                continue
            K = (p + q) // 4
            c = cert_value(K, q) < 1 - 1e-9  # exact value 1 occurs (e.g. p = 1000121, q = 11)
            w = witness(K, q)
            key = "forced" if legendre_symbol(q, p) == -1 else "unforced"
            s = stats[key]
            s[0] += 1
            s[1] += c
            s[2] += w is not None
            if c and w is None:
                viol += 1
            if w is not None:
                u, v = w
                y = p * (K // u) * (u + v) // q
                z = p * (K // v) * (u + v) // q
                assert Fraction(4, p) == Fraction(1, K) + Fraction(1, y) + Fraction(1, z)
    print("cert-without-witness violations:", viol)
    for k, (n, c, w) in stats.items():
        print(f"{k}: windows {n}, cert holds {c}, signed-squarefree witness {w}")


if __name__ == "__main__":
    lo, hi, qmax = (int(a) for a in (sys.argv[1:] or ["1000000", "1003000", "60"]))
    main(lo, hi, qmax)
