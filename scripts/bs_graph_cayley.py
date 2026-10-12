"""Chord/tangent (Manin) moves on the Cayley cubic sigma3(X)=0 restricted to ES points.

ES point for n: primitive (X0,X1,X2,X3) = (-n,4x,4y,4z)/g with 4/n = 1/x+1/y+1/z.
We classify the third point R of chords PQ and of tangent sections at P:
  'ES'      : one coordinate negative, three positive, the three positive ones = 0 mod 4  (ES point for N=|neg|)
  'pos1'    : sign pattern (-,+,+,+) but not all three positives = 0 mod 4 (a 1/N = 3 unit fractions point)
  'other'   : any other sign pattern (signed solutions), or on a line (zero coordinate)
Usage: python bs_graph_cayley.py NMAX
"""
import sys, itertools
from math import gcd
from collections import Counter


def es_solutions(n):
    """all 4/n = 1/x+1/y+1/z, x<=y<=z"""
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        num, den = 4 * x - n, n * x  # remainder num/den
        if num <= 0:
            continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            zn, zd = num * y - den, den * y
            if zn > 0 and zd % zn == 0:
                out.append((x, y, zd // zn))
    return out


def prim(v):
    g = 0
    for a in v:
        g = gcd(g, a)
    if g == 0:
        return None
    v = tuple(a // g for a in v)
    # normalise sign: majority positive
    if sum(1 for a in v if a < 0) > 2:
        v = tuple(-a for a in v)
    return v


def grad(P):
    X = P
    return [X[(i+1) % 4]*X[(i+2) % 4] + X[(i+1) % 4]*X[(i+3) % 4] + X[(i+2) % 4]*X[(i+3) % 4] for i in range(4)]


def s3(X):
    a, b, c, d = X
    return a*b*c + a*b*d + a*c*d + b*c*d


def chord(P, Q):
    A = sum(g*q for g, q in zip(grad(P), Q))
    B = sum(g*p for g, p in zip(grad(Q), P))
    return prim([B*p - A*q for p, q in zip(P, Q)])


def classify(R):
    if R is None or 0 in R:
        return 'other', None
    neg = [a for a in R if a < 0]
    if len(neg) != 1:
        return 'other', None
    N = -neg[0]
    pos = [a for a in R if a > 0]
    if all(a % 4 == 0 for a in pos):
        return 'ES', N
    return 'pos1', N


def tangent_points(P, H):
    """third points of lines P + tV, V in tangent plane, V small integer vectors"""
    gP = grad(P)
    out = []
    for V in itertools.product(range(-H, H+1), repeat=4):
        if sum(g*v for g, v in zip(gP, V)) != 0:
            continue
        C = sum(g*p for g, p in zip(grad(V), P))
        sV = s3(V)
        R = [sV*p - C*v for p, v in zip(P, V)]
        if all(r == 0 for r in R):
            continue
        out.append(prim(R))
    return out


def isprime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    pts = []
    for n in range(2, NMAX+1):
        for (x, y, z) in es_solutions(n):
            P = prim((-n, 4*x, 4*y, 4*z))
            assert s3(P) == 0
            pts.append(P)
    pts = sorted(set(pts))
    print('ES points with n<=%d: %d' % (NMAX, len(pts)))
    cnt = Counter(); esN = Counter(); newprimes = set()
    for P, Q in itertools.combinations(pts, 2):
        R = chord(P, Q)
        c, N = classify(R)
        cnt[c] += 1
        if c == 'ES':
            nP, nQ = -min(P), -min(Q)
            esN['N divisible by nP or nQ' if (N % nP == 0 or N % nQ == 0) else 'new N'] += 1
            if isprime(N) and N not in (nP, nQ):
                newprimes.add(N)
    print('chords:', dict(cnt), dict(esN))
    print('prime N reached by chords (not an endpoint n):', sorted(newprimes)[:30], len(newprimes))
    tc = Counter(); tprimes = set()
    for P in pts[:60]:
        for R in tangent_points(P, 3):
            c, N = classify(R)
            tc[c] += 1
            if c == 'ES' and isprime(N):
                tprimes.add(N)
    print('tangent sections (first 60 pts, |V|<=3):', dict(tc), 'ES primes:', sorted(tprimes)[:30])
