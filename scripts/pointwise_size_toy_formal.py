#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 4 -- toy check of Theorem M / Theorem C on actual primes.

Bounded witness-producing program PI(p), p = 24q+1:
    for a in A (Type II windows, Thm 3.1(B)):  x=(p+a)/4, for d | x^2: a | d+x  -> SUCCESS
    for m in B (Type I  windows, Thm 3.1(A)):  z=(pm+1)/4, for d | z^2: m | d+z  -> SUCCESS
    otherwise FAIL.
Every window is a linear polynomial in q: x = g*h(q), h primitive.

For a profinite point given by residues q*_l mod l^E_l (l in LAM) the script
  1. computes the FORMAL run (formal primes r_h = h(q)/C_h, residues from q*), independently
     of any actual factorisation;
  2. finds actual admissible q (q = q* mod M, p and all r_h prime) by a sieve, runs the
     actual program (sympy factorint) and checks that its output equals the formal output;
  3. for a sample of NON-admissible q in the same class (p prime only), records successes
     and checks that each success happens at a window whose r_h is composite and that the
     solution's p-free denominator has a QNR prime factor (Lemma CT).

Point 'sq' is square-mimicking (24q*+1 a nonzero square mod every l in LAM): Theorem C
predicts formal output FAIL.  Point 'nsq' differs only at l=7 (p a non-residue mod 7),
to show that the formal engine is not trivially FAIL.

Usage: PYTHONPATH=scripts uv run python scripts/pointwise_size_toy_formal.py [KMAX]
"""
import sys
import random
from math import gcd
import numpy as np
from sympy import factorint, isprime, primerange
from sympy.ntheory.modular import crt

A = [3, 7, 11]
B = [3, 7]
LAM = {2: 4, 3: 2, 5: 1, 7: 1, 11: 1}          # l -> E_l
POINTS = {
    'sq':  {2: 1, 3: 2, 5: 0, 7: 0, 11: 2},     # residues q*_l mod l^E_l
    'nsq': {2: 1, 3: 2, 5: 0, 7: 6, 11: 2},
}


def windows():
    """list of (kind, modulus, g, (alpha,beta)) with window(q) = g*(alpha q+beta)."""
    out = []
    for a in A:                     # x = (24q+1+a)/4 = 6q + (a+1)/4
        s = (a + 1) // 4
        g = gcd(6, s)
        out.append(('II', a, g, (6 // g, s // g)))
    for m in B:                     # z = (24mq+m+1)/4 = 6m q + (m+1)/4
        s = (m + 1) // 4
        g = gcd(6 * m, s)
        out.append(('I', m, g, (6 * m // g, s // g)))
    return out


def vl(n, l):
    v = 0
    while n % l == 0:
        n //= l
        v += 1
    return v


def setup(point):
    M = 1
    for l, E in LAM.items():
        M *= l ** E
    qt = int(crt([l ** E for l, E in LAM.items()], [point[l] for l in LAM])[0])
    # square-mimicking status of p* = 24q*+1
    status = {}
    for l, E in LAM.items():
        pv = (24 * qt + 1) % (l ** E)
        if l == 2:
            status[l] = ((24 * qt + 1) % 8 == 1)
        else:
            status[l] = pow(pv % l, (l - 1) // 2, l) == 1
    wins = windows()
    polys = {}
    for w in wins:
        alpha, beta = w[3]
        val = alpha * qt + beta
        C = 1
        for l, E in LAM.items():
            v = vl(val, l)
            assert v < E, ("precision", w, l)
            C *= l ** v
        polys[w[3]] = C
    # nondegeneracy outside LAM is enforced in the search by requiring r_h prime.
    return M, qt, wins, polys, status


def formal_run(M, qt, wins, polys):
    """Formal output: decide every test from q* residues only."""
    for kind, mod, g, h in wins:
        alpha, beta = h
        C = polys[h]
        K = g * C                              # window = K * r,  r formal prime
        r_mod = ((alpha * qt + beta) // C) % mod   # valid since mod | M/C (checked)
        assert (M // C) % mod == 0
        x_mod = (K * r_mod) % mod
        Kfac = factorint(K * K)
        cdivs = [1]
        for l, e in Kfac.items():
            cdivs = [c * l ** i for c in cdivs for i in range(e + 1)]
        for c in cdivs:
            for j in range(3):
                d_mod = (c * pow(r_mod, j, mod)) % mod
                if (d_mod + x_mod) % mod == 0:
                    return ('SUCCESS', kind, mod, c, j)
    return ('FAIL',)


def actual_run(p):
    for a in A:
        x = (p + a) // 4
        for d in divisors_sq(x):
            if (d + x) % a == 0:
                sol = (x, p * (x + d) // a, p * (x + x * x // d) // a)
                assert 4 * sol[0] * sol[1] * sol[2] == p * (sol[0] * sol[1] + sol[1] * sol[2] + sol[0] * sol[2])
                return ('SUCCESS', 'II', a, sol)
    for m in B:
        z = (p * m + 1) // 4
        for d in divisors_sq(z):
            if (d + z) % m == 0:
                sol = ((z + d) // m, (z + z * z // d) // m, p * z)
                assert 4 * sol[0] * sol[1] * sol[2] == p * (sol[0] * sol[1] + sol[1] * sol[2] + sol[0] * sol[2])
                return ('SUCCESS', 'I', m, sol)
    return ('FAIL',)


def divisors_sq(n):
    ds = [1]
    for l, e in factorint(n).items():
        ds = [d * l ** i for d in ds for i in range(2 * e + 1)]
    return sorted(ds)


def qnr_factor(n, p):
    return any(pow(l, (p - 1) // 2, p) == p - 1 for l in factorint(n))


def search(M, qt, polys, KMAX, chunk=2_000_000):
    """admissible q = qt + M k, k < KMAX: p prime and every r_h prime."""
    forms = [(24, 1, 1)] + [(al, be, C) for (al, be), C in polys.items()]
    small = [l for l in primerange(13, 3000) if l not in LAM]
    found = []
    for k0 in range(0, KMAX, chunk):
        ks = np.arange(k0, min(k0 + chunk, KMAX), dtype=np.int64)
        alive = np.ones(len(ks), dtype=bool)
        for (al, be, C) in forms:
            for l in small:
                # (al*(qt+M k)+be)/C = 0 mod l  <=> al*M*k = -(al*qt+be) mod l
                c1 = (al * M) % l
                c0 = (al * qt + be) % l
                k_root = (-c0 * pow(c1, -1, l)) % l
                alive &= (ks % l) != k_root
        for k in ks[alive]:
            q = qt + M * int(k)
            if all(isprime((al * q + be) // C) for (al, be, C) in forms):
                found.append(q)
    return found


def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6_000_000
    random.seed(1)
    ok = True
    for name, point in POINTS.items():
        M, qt, wins, polys, status = setup(point)
        fo = formal_run(M, qt, wins, polys)
        print(f"== point {name}: M={M}, q*={qt}; p* square mod l: {status}")
        print(f"   S = P and {sorted(polys)} with C_h = {[polys[h] for h in sorted(polys)]}")
        print(f"   formal output: {fo}")
        adm = search(M, qt, polys, KMAX)
        mism = 0
        for q in adm:
            ar = actual_run(24 * q + 1)
            if ar[0] != fo[0] or (fo[0] == 'SUCCESS' and (ar[1], ar[2]) != (fo[1], fo[2])):
                mism += 1
        print(f"   admissible q found (k<{KMAX}): {len(adm)}; actual output != formal: {mism}")
        if adm:
            print(f"   e.g. q={adm[0]}, p={24*adm[0]+1}")
        ok &= (mism == 0) and len(adm) > 0
        if name == 'sq':
            ok &= fo[0] == 'FAIL'
            # non-admissible sample in the same class
            ns = succ = viol = 0
            while ns < 3000:
                q = qt + M * random.randrange(10 ** 5, 10 ** 7)
                p = 24 * q + 1
                if not isprime(p):
                    continue
                ns += 1
                ar = actual_run(p)
                if ar[0] == 'SUCCESS':
                    succ += 1
                    kind, mod, sol = ar[1], ar[2], ar[3]
                    w = [w for w in wins if w[0] == kind and w[1] == mod][0]
                    al, be = w[3]
                    r = (al * q + be) // polys[w[3]]
                    pfree = [s for s in sol if s % p]
                    if isprime(r) or not any(qnr_factor(s, p) for s in pfree):
                        viol += 1
            print(f"   non-admissible sample (p prime, same class): {ns}, successes {succ}; "
                  f"successes with r_h prime or no QNR factor: {viol}")
            ok &= viol == 0
    print("OK" if ok else "FAILED")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
