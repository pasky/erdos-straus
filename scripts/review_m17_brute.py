"""R83 from-scratch brute force: ET Prop 1.9 classes, read straight off the statement
(arXiv:1107.1010 Prop 1.9), restricted to moduli M <= MMAX, intersected with the
17-generic line {x : x_q = 1 for q != 17}.  Does NOT use the T-generic table.

A class r mod M (M = 17^k N, 17 !| N) meets the line iff r = 1 mod N; its trace is the
box r mod 17^k.  Output: pickle {(fam, k, r mod 17^k)} for k <= KMAX (incl. k = 0 boxes,
which would be classes containing the whole line).

usage: review_m17_brute.py MMAX KMAX out.pkl
"""
import sys, pickle
from math import gcd
from sympy import divisors, sqrt_mod

MMAX, KMAX, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
P = 17


def split(M):
    k = 0
    while M % P == 0:
        M //= P; k += 1
    return k, M


boxes = set()


def emit(fam, M, r, params):
    k, N = split(M)
    if k > KMAX:
        return
    if gcd(r, M) != 1:
        return  # non-primitive: never contains units
    if r % N != 1 % N:
        return
    boxes.add((fam, k, r % P**k))
    if k == 0:
        print("LEVEL-0 CLASS", fam, M, r, params, flush=True)


def crt(r1, m1, r2, m2):
    # m1, m2 coprime
    t = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (r1 + m1 * t) % (m1 * m2)


# I1: n = -f mod 4ad, f | 4a^2 d + 1
for a in range(1, MMAX // 4 + 1):
    for d in range(1, MMAX // (4 * a) + 1):
        M = 4 * a * d
        _, N = split(M)
        if N == M and False:
            pass
        for f in divisors(4 * a * a * d + 1):
            emit("I1", M, (-f) % M, (a, d, f))
print("I1 done", len(boxes), flush=True)

# I2: n = -f mod 4ac, n = -c/a mod f, (4ac, f) = 1 ; M = 4acf
for a in range(1, MMAX // 4 + 1):
    for c in range(1, MMAX // (4 * a) + 1):
        for f in range(1, MMAX // (4 * a * c) + 1):
            if gcd(4 * a * c, f) != 1:
                continue
            r = crt((-f) % (4 * a * c), 4 * a * c, (-c * pow(a, -1, f)) % f if f > 1 else 0, f)
            emit("I2", 4 * a * c * f, r, (a, c, f))
print("I2 done", len(boxes), flush=True)

# I3: n = -f mod 4cd, n^2 = -4c^2 d mod f, (4cd, f) = 1 ; M = 4cdf
for c in range(1, MMAX // 4 + 1):
    for d in range(1, MMAX // (4 * c) + 1):
        for f in range(1, MMAX // (4 * c * d) + 1):
            if gcd(4 * c * d, f) != 1:
                continue
            if f == 1:
                roots = [0]
            else:
                roots = sqrt_mod((-4 * c * c * d) % f, f, all_roots=True) or []
            for s in roots:
                emit("I3", 4 * c * d * f, crt((-f) % (4 * c * d), 4 * c * d, s, f), (c, d, f))
print("I3 done", len(boxes), flush=True)

# I4: n = -1/e mod 4ab, e | a+b, (e,4ab)=1 ; II1: n = -e mod 4ab, same conditions
for a in range(1, MMAX // 4 + 1):
    for b in range(1, MMAX // (4 * a) + 1):
        M = 4 * a * b
        for e in divisors(a + b):
            if gcd(e, M) != 1:
                continue
            emit("I4", M, (-pow(e, -1, M)) % M, (a, b, e))
            emit("II1", M, (-e) % M, (a, b, e))
print("I4/II1 done", len(boxes), flush=True)

# II2: n = -4a^2 d mod f, 4ad | f+1 ; M = f
for a in range(1, MMAX // 4 + 1):
    for d in range(1, MMAX // (4 * a) + 1):
        for f in range(4 * a * d - 1, MMAX + 1, 4 * a * d):
            emit("II2", f, (-4 * a * a * d) % f, (a, d, f))
print("II2 done", len(boxes), flush=True)

# II3: n = -4a^2 d - e mod 4ade, (4ad, e) = 1 ; M = 4ade
for a in range(1, MMAX // 4 + 1):
    for d in range(1, MMAX // (4 * a) + 1):
        for e in range(1, MMAX // (4 * a * d) + 1):
            if gcd(4 * a * d, e) != 1:
                continue
            M = 4 * a * d * e
            emit("II3", M, (-4 * a * a * d - e) % M, (a, d, e))
print("II3 done", len(boxes), flush=True)

pickle.dump(boxes, open(OUT, "wb"))
from collections import Counter
print(Counter((f, k) for f, k, _ in boxes))
