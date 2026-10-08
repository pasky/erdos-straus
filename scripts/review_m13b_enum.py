"""R95 from-scratch §4 re-run: (1) enumerate all ES solutions of 4/N (x<=y<=z) for T-units N<=NMAX,
(2) invert by reviewer-derived inverse maps of Lemmas 2.1-2.4 (shape A: II3/I3/I1, B: II1/I4, C: II2, D: I2),
(3) keep data whose family constraints + T-free box conditions hold literally (ET Prop 1.9 classes),
(4) report data containing x* and per-cell coverage.  usage: review_m13b_enum.py NMAX out.pkl"""
import sys, pickle, itertools
from math import gcd, isqrt
from fractions import Fraction as Fr
sys.path.insert(0, __import__('os').path.dirname(__file__))
from review_m13b_lem11 import classres, tpart  # reviewer's own literal ET classes
T = (11, 13)
def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1 if p == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divs(fd):
    out = [1]
    for p, e in fd.items(): out = [d * p**k for d in out for k in range(e + 1)]
    return out
def es(N):
    sols = []; fN = factor(N)
    for x in range(N // 4 + 1, 3 * N // 4 + 1):
        num = 4 * x - N; den = N * x
        if num <= 0: continue
        g = gcd(num, den); p, q = num // g, den // g
        fq = dict(fN); 
        for pp, e in factor(x).items(): fq[pp] = fq.get(pp, 0) + e
        fq = {pp: e for pp, e in fq.items() if q % pp == 0}
        for pp in fq:
            e = 0; t = q
            while t % pp == 0: t //= pp; e += 1
            fq[pp] = 2 * e
        for dl in divs(fq):
            if dl > q or (q + dl) % p: continue
            y = (q + dl) // p; z2 = q + q * q // dl
            if z2 % p: continue
            z = z2 // p
            if y >= x: sols.append((x, y, z))
    return sols
def sqf_split(K1, K2, K3):  # all delta with K_i = delta * square
    out = []
    g = gcd(gcd(K1, K2), K3)
    for dl in divs(factor(g)) if g > 1 else [1]:
        r = [K // dl for K in (K1, K2, K3)]
        s = [isqrt(v) for v in r]
        if all(v * v == w for v, w in zip(s, r)): out.append((dl, s))
    return out
def tsplits(N):  # N = 11^i 13^j
    i = j = 0; t = N
    while t % 11 == 0: t //= 11; i += 1
    while t % 13 == 0: t //= 13; j += 1
    return i, j
def tunits_le(L):
    return [11**i * 13**j for i in range(12) for j in range(12) if 1 < 11**i * 13**j <= L]
def lam_decomp(lam):  # lam = aT^2 dT
    i, j = tsplits(lam); out = []
    for ia in range(i // 2 + 1):
        for ja in range(j // 2 + 1):
            aT = 11**ia * 13**ja; out.append((aT, lam // (aT * aT)))
    return out
def ok_family(fam, P):  # literal ET family constraint and T-free box condition r=1 mod M'
    x, y, z = P
    if min(P) < 1: return False
    if fam == 'I1' and (4*x*x*y+1) % z: return False
    if fam in ('I2', 'I3', 'II3') and gcd(4*x*y, z) != 1: return False
    if fam in ('I4', 'II1') and ((x+y) % z or gcd(z, 4*x*y) != 1): return False
    if fam == 'II2' and (z+1) % (4*x*y): return False
    R, M = classres(fam, P); MT = tpart(M); Mp = M // MT
    rs = sorted({r % MT for r in R if r % Mp == 1 % Mp})
    return (M, MT, rs) if rs else False
def invert(N, sol):
    found = set()
    for X, Y, Z in set(itertools.permutations(sol)):
        # shape A: X=d'mj, Y=lam a'd'j, Z=B lam a'd'm, N=B lam
        for lam in [u for u in tunits_le(N) + [1] if N % u == 0]:
            B = N // lam
            if Y % lam or Z % (B*lam): continue
            P_, Q_, R_ = Y // lam, Z // (B*lam), X
            if (P_*Q_) % R_ or (P_*R_) % Q_ or (Q_*R_) % P_: continue
            for dp, (ap, j, m) in sqf_split(P_*Q_//R_, P_*R_//Q_, Q_*R_//P_):
                if tpart(ap*dp) > 1: continue
                for aT, dT in lam_decomp(lam):
                    a, d = aT*ap, dT*dp; e = 4*ap*dp*m - 1
                    if e < 1: continue
                    if tpart(e) == B: found.add(('II3', (a, d, e))); found.add(('I3', (a, d, e)))
                    if B == 1: found.add(('I1', (a, d, e)))
        # shape B: X=iab, Y=iac, Z=ibc, N=(ab)_T
        if (X*Y) % Z == 0 and (X*Z) % Y == 0 and (Y*Z) % X == 0:
            for i, (a, b, c) in sqf_split(X*Y//Z, X*Z//Y, Y*Z//X):
                if (a+b) % c: continue
                e = (a+b)//c
                if tpart(a*b) == N: found.add(('II1', (a, b, e))); found.add(('I4', (a, b, e)))
        # shape C: X=amdF, Y=ajd, Z=mjd, N=F=f_T
        F = N
        if (X*Y) % (Z*F) == 0 and (X*Z) % (Y*F) == 0 and (Y*Z*F) % X == 0:
            for d, (a, m, j) in sqf_split(X*Y//(Z*F), X*Z//(Y*F), Y*Z*F//X):
                f = 4*a*d*m - 1
                if tpart(f) == F: found.add(('II2', (a, d, f)))
        # shape D: X=cth, Y=ath, Z=B a c t, N=AB
        for A in [u for u in tunits_le(N) + [1] if N % u == 0]:
            B = N // A
            if (B*X*Y) % Z or (X*Z) % (Y*B) or (Y*Z) % (X*B): continue
            for t, (h, c, a) in sqf_split(B*X*Y//Z, X*Z//(Y*B), Y*Z//(X*B)):
                f = 4*(a*c//tpart(a*c))*t - 1
                if f >= 1 and tpart(f) == B and tpart(a*c) == A: found.add(('I2', (a, c, f)))
    out = []
    for fam, P in found:
        r = ok_family(fam, P)
        if r: out.append((fam, P, r))
    return out
if __name__ == '__main__':
    NMAX = int(sys.argv[1]); res = {}
    for N in sorted(tunits_le(NMAX)):
        S = es(N); D = []
        for s in S: D += invert(N, s)
        D = sorted(set((f, P, (M, MT, tuple(rs))) for f, P, (M, MT, rs) in D))
        res[N] = (len(S), D)
        xs = [(f, P, M) for f, P, (M, MT, rs) in D if 2 % MT in rs]
        print(f'N={N}: {len(S)} ES sols, {len(D)} data; x* in: {xs}', flush=True)
    pickle.dump(res, open(sys.argv[2], 'wb'))
