"""R261 from-scratch checker: Lemma-3.1 window certificates (CAP_DOWN Lemma 3.1) for 4/p.

Independent of scripts/z22_*.  For prime p = 1 (mod 4), window m = 3 (mod 4), gcd(m,p)=1, x = K = (p+m)/4:
solutions <-> D1 = p*K*prod s^delta_s with D1 = -pK (mod m), i.e. prod s^delta_s = -1 (mod m).
Allowed: s | 2K: |delta_s| <= b_s; s = p: delta_p in {-1,0,1}; odd s | K additionally delta_s = b_s + 2k, 1<=k<=e.
least_cap(p, m, emax) = least e <= emax with a certificate (or None).  'inf' cap = saturation (emax huge).
Also: rebuild(p, m, vec) -> (x, y, z) and check_def11 -> independent exact check of ES^{(y,e)}.
"""
import sys
from fractions import Fraction
from math import gcd, isqrt
from sympy import factorint, jacobi_symbol, isprime, primerange
from sympy.ntheory import n_order


def residues_for(s, b, e, kind, m):
    """dict residue -> (delta, cap) with minimal cap per residue."""
    out = {}
    if kind == 'p':
        D = [(d, 0) for d in (-1, 0, 1)]
    else:
        D = [(d, 0) for d in range(-b, b + 1)]
        if kind == 'odd':
            D += [(b + 2 * k, k) for k in range(1, e + 1)]
    for d, c in D:
        r = pow(s, d, m)  # python handles negative exponents mod m
        if r not in out or out[r][1] > c:
            out[r] = (d, c)
    return out


def least_cap(p, m, emax, fac=None, use_p=True):
    assert m % 4 == 3 and (p + m) % 4 == 0 and gcd(m, p) == 1
    K = (p + m) // 4
    fac = fac or factorint(K)
    # DP over generators: residue -> minimal cap (and witness)
    best = {1 % m: (0, ())}
    gens = [(s, b, 'two' if s == 2 else 'odd') for s, b in fac.items()]
    if use_p:
        gens.append((p, 1, 'p'))
    for s, b, kind in gens:
        R = residues_for(s, b, emax, kind, m)
        nb = {}
        for r, (c0, v0) in best.items():
            for t, (d, c) in R.items():
                rr = r * t % m
                cc = max(c0, c)
                if rr not in nb or nb[rr][0] > cc:
                    nb[rr] = (cc, v0 + ((s, d),))
        best = nb
    return best.get((m - 1) % m)


def rebuild(p, m, vec):
    K = (p + m) // 4
    N = p * K
    D1 = Fraction(N)
    for s, d in vec:
        D1 *= Fraction(s) ** d
    assert D1.denominator == 1
    D1 = D1.numerator
    assert (N + D1) % m == 0
    y = (N + D1) // m
    z = Fraction(N * y, D1)
    return K, y, z


def check_def11(p, x, y, z, e):
    if Fraction(4, p) != Fraction(1, x) + Fraction(1, y) + z ** -1:
        return False
    den = z.denominator
    r = isqrt(den)
    if r * r != den or r % 2 == 0 or gcd(r, p) != 1:
        return False
    for l, v in factorint(r).items():
        if y % l or v > e:
            return False
    return True


if __name__ == '__main__':
    p = int(sys.argv[1]); M = int(sys.argv[2]); E = int(sys.argv[3])
    for m in range(3, M + 1, 4):
        if gcd(m, p) != 1:
            continue
        K = (p + m) // 4
        fac = factorint(K)
        syms = {s: jacobi_symbol(s, p) for s in fac}
        res = least_cap(p, m, E, fac)
        print(m, fac, 'symbols', syms, '(m/p)=', jacobi_symbol(m, p), 'cap', res)
