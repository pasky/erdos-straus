"""O131b (3): ideal classes of Type I solutions for fixed (p,d).  Solution (a,b,c,d) of prime p <-> ideal a | alpha,
N(a) = f = 4acd - p, Heegner form [f, 4ad, de] (disc -4d, e = (4a^2 d+1)/f).  For each d with h(-4d) > #genus
classes, collect class histograms over primes p <= 2e4 and test (i) one genus per (p,d), (ii) uniformity inside the
genus (chi^2 vs multinomial; E[X^2] = g-1 under uniform), (iii) whether any class is always/never hit."""
import numpy as np
from sympy import isprime
from math import gcd
from exf_load import load
def reduce(A, B, C):
    while True:
        if C < A or (C == A and B < 0): A, B, C = C, -B, A
        elif B > A or B <= -A:
            k = (A - B) // (2 * A); B, C = B + 2 * k * A, A * k * k + B * k + C
        else: return (A, B, C)
def classes(D):  # reduced forms of disc -D (D = 4d), all, primitive or not
    out = []
    for A in range(1, int((D / 3) ** 0.5) + 1):
        for B in range(-A + 1, A + 1):
            if (B * B + D) % (4 * A) == 0:
                C = (B * B + D) // (4 * A)
                if C >= A and not (C == A and B < 0) and gcd(gcd(A, B), C) == 1: out.append((A, B, C))
    return out
if __name__ == '__main__':
    T1, _ = load('data/exf/n2e4')
    n = T1['n'].astype(np.int64); isp = np.array([isprime(int(x)) for x in range(int(n.max()) + 1)])
    for d in (14, 17, 21, 26, 29, 30, 34, 41, 46, 65):
        cl = classes(4 * d); h = len(cl); idx = {f: i for i, f in enumerate(cl)}
        sel = (T1['d'] == d) & isp[n]
        R = T1[sel]; a = R['a'].astype(np.int64); c = R['c'].astype(np.int64); p = R['n'].astype(np.int64)
        f = 4 * a * c * d - p; e = (4 * a * a * d + 1) // f
        lab = np.array([idx[reduce(int(F), int(4 * A * d), int(E * d))] for F, A, E in zip(f, a, e)])
        hist = {}
        for P, L in zip(p, lab): hist.setdefault(int(P), np.zeros(h, int))[L] += 1
        # genus of a class = set of classes reached together; check one genus per p
        support = [frozenset(np.nonzero(v)[0]) for v in hist.values()]
        genera = []
        for s in support:
            for G in genera:
                if G & s: G |= s; break
            else: genera.append(set(s))
        g = max(len(G) for G in genera)
        X2 = []; hitfrac = np.zeros(h); cnt = np.zeros(h)
        for v in hist.values():
            G = sorted(next(G for G in genera if np.nonzero(v)[0][0] in G)); m = v[G].sum()
            if len(G) > 1 and m >= 2 * len(G): X2.append(((v[G] - m / len(G)) ** 2).sum() / (m / len(G)))
            cnt[G] += 1; hitfrac[G] += v[G] > 0
        tot = sum(hist.values())
        gstr = '; '.join('/'.join(f'{cl[i]}:{tot[i]}' for i in sorted(G)) for G in genera if len(G) > 1)
        # overdispersion source: within one (p,d), how often do solutions share the same c (same alpha)?
        print(f'   class totals inside genera: {gstr}')
        print(f'd={d}: h(-4d)={h}, genus size g={g}, #genera seen={len(genera)}, primes={len(hist)}, '
              f'mean X^2={np.mean(X2):.2f} (uniform: {g-1}), #p used={len(X2)}, '
              f'P(class hit) min/max = {np.min(hitfrac[cnt>0]/cnt[cnt>0]):.2f}/{np.max(hitfrac[cnt>0]/cnt[cnt>0]):.2f}')
    