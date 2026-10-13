"""R166 from-scratch: Haar mass of the cylinder C = {u = u0 (mod T^3)} (slice x = 1 off T, A = T^k, q = p)
covered by Case B families with deg L' <= dl, j <= jm. A family (L', j, g, E) covers {u = -E mod T^{k+j}}
iff E monic, E | D = 1 + T^{k+j} g L', E = -1 (mod L') (and -E in C).
Factorisation by trial division with all monic irreducibles of degree <= deg D / 2.
usage: review_ff2_mass.py p k u0(low-first) dl jm"""
import sys
from itertools import product as iprod
from review_ff2_poly import *

p, k = int(sys.argv[1]), int(sys.argv[2]); setp(p)
u0 = tr([int(x) for x in sys.argv[3].split(',')])
dl, jm = int(sys.argv[4]), int(sys.argv[5])
K = k + jm  # resolution
maxD = k + jm + jm + 2 * dl
irr = []
for d in range(1, maxD // 2 + 1):
    for f in monics(d):
        if all(not divides(g, f) for g in irr if 2 * deg(g) <= d):
            irr.append(f)


def factor(D):
    fs = []
    x = D
    for f in irr:
        if 2 * deg(f) > deg(x):
            break
        e = 0
        while True:
            q, r = dm(x, f)
            if r:
                break
            x, e = q, e + 1
        if e:
            fs.append((f, e))
    if deg(x) > 0:
        fs.append((x, 1))
    return fs


def divisors(fs):
    ds = [(1,)]
    for f, e in fs:
        new = []
        for d in ds:
            pw = (1,)
            for i in range(e + 1):
                new.append(mul(d, pw))
                pw = mul(pw, f)
        ds = new
    return ds


def key(a, n):
    a = mod(a, Tpow(n))
    return tuple(list(a) + [0] * (n - len(a)))


covered = set()  # residues mod T^K inside C
bylevel = {}
nfam = 0
for dL in range(dl + 1):
    for Lp in monics(dL):
        if Lp[0] == 0:
            continue
        gps = [d for d in monics_upto(dL) if divides(d, Lp)]
        for j in range(jm + 1):
            L = mul(Tpow(j), Lp)
            for gp in gps:
                for gam in range(j + 1):
                    g = mul(Tpow(gam), gp)
                    D = add((1,), mul(Tpow(k), mul(g, L)))
                    for E in divisors(factor(D)):
                        if dL and mod(add(E, (1,)), Lp):
                            continue
                        mu = key(neg(E), k + j)
                        if key(neg(E), 3) != key(u0, 3) or k + j < 3:
                            continue
                        nfam += 1
                        for ext in iprod(range(p), repeat=K - (k + j)):
                            covered.add(mu + ext)
    print("deg L' <=", dL, "families", nfam, "union mass of C", len(covered) / p ** (K - 3), flush=True)
