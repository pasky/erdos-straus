"""R188: independent recomputation of STERILE_STEER Sec. 2 (EVIDENCE): Mordell height h(p) and least escape
modulus E for primes near the sterile point x(5) (r = 17), near 1, in random non-residue cells, and random.

Own method (not the author's residue tables): for each prime p, every class of modulus <= X containing p is found
by testing the class *conditions* of ET Prop 1.9 directly against p mod m (vectorised over all parameter tuples).
Witnesses (least-h class and least-E class) are re-solved at p with review_ss_lib.es_solution (ET Sec. 10 tuple,
exact Fraction check of 4/p = 1/x+1/y+1/z).

usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_ss_escape.py X NP SEED B [B ...]
"""
import sys, os, random, pickle
from math import gcd
import numpy as np
import sympy
import review_ss_lib as L

X = int(sys.argv[1]); NP = int(sys.argv[2]); SEED = int(sys.argv[3]); BS = [int(b) for b in sys.argv[4:]]
Q = X // 4
cache = f'/tmp/review_ss_tab_{X}.pkl'
if os.path.exists(cache):
    T = pickle.load(open(cache, 'rb'))
else:
    T = {}
    I1 = []; P2 = []
    for a in range(1, Q + 1):
        for d in range(1, Q // a + 1):
            M = 4 * a * d
            for f in sympy.divisors(4 * a * a * d + 1):
                I1.append((a, d, f, M))
            for e in sympy.divisors(a + d):
                if gcd(e, M) == 1:
                    P2.append((a, d, e, M))
    T['I1'] = np.array(I1, dtype=np.int64); T['I4II1'] = np.array(P2, dtype=np.int64)
    II2 = []
    for f in range(3, X + 1, 4):
        g = (f + 1) // 4
        for a in sympy.divisors(g):
            for d in sympy.divisors(g // a):
                II2.append((a, d, f, f))
    T['II2'] = np.array(II2, dtype=np.int64)
    TR = []
    for x in range(1, Q + 1):
        for y in range(1, Q // x + 1):
            for z in range(1, Q // (x * y) + 1):
                if gcd(4 * x * y, z) == 1:
                    TR.append((x, y, z, 4 * x * y * z))
    T['TRI'] = np.array(TR, dtype=np.int64)
    pickle.dump(T, open(cache, 'wb'))
print({k: len(v) for k, v in T.items()}, flush=True)

FAC = {}
def fac(M):
    if M not in FAC:
        FAC[M] = sympy.factorint(M)
    return FAC[M]


def hits(p):
    pm = np.array([0, 0] + [p % m for m in range(2, X + 1)], dtype=np.int64)
    out = []  # (M, fam, params)
    a, d, f, M = T['I1'].T
    for i in np.nonzero((pm[M] + f) % M == 0)[0]:
        out.append((int(M[i]), 'I1', (int(a[i]), int(d[i]), int(f[i]))))
    a, b, e, M = T['I4II1'].T
    for i in np.nonzero((pm[M] * e + 1) % M == 0)[0]:
        out.append((int(M[i]), 'I4', (int(a[i]), int(b[i]), int(e[i]))))
    for i in np.nonzero((pm[M] + e) % M == 0)[0]:
        out.append((int(M[i]), 'II1', (int(a[i]), int(b[i]), int(e[i]))))
    a, d, f, M = T['II2'].T
    for i in np.nonzero((pm[f] + 4 * a * a * d) % f == 0)[0]:
        out.append((int(M[i]), 'II2', (int(a[i]), int(d[i]), int(f[i]))))
    x, y, z, M = T['TRI'].T
    m1 = 4 * x * y
    c1 = (pm[m1] + z) % m1 == 0
    for i in np.nonzero(c1 & ((pm[z] * x + y) % z == 0))[0]:
        out.append((int(M[i]), 'I2', (int(x[i]), int(y[i]), int(z[i]))))
    for i in np.nonzero(c1 & ((pm[z] * pm[z] + 4 * x * x * y) % z == 0))[0]:
        out.append((int(M[i]), 'I3', (int(x[i]), int(y[i]), int(z[i]))))
    for i in np.nonzero((pm[M] + 4 * x * x * y + z) % M == 0)[0]:
        out.append((int(M[i]), 'II3', (int(x[i]), int(y[i]), int(z[i]))))
    return out


def escape(M, p):
    E = 1
    for q, v in fac(M).items():
        if (p - 1) % q ** v:
            E *= q ** v
    return E


rng = random.Random(SEED)
def prime_in(mod, res, lo):
    while True:
        p = rng.randrange(lo // mod, 2 * lo // mod) * mod + res
        if sympy.isprime(p):
            return p

r, u, Lv = 17, 5, 4
NR = [v for v in range(1, 17) if pow(v, 8, 17) == 16]
for B in BS:
    lcm = int(sympy.ilcm(*range(1, B + 1))); QB = lcm // 17 ** sympy.multiplicity(17, lcm)
    lo = max(10 ** 16, QB * r ** Lv * 1000)
    for pop in 'ABCD':
        rows = []
        for _ in range(NP):
            if pop == 'A':
                mod = QB * r ** Lv; res = L.crt(1, QB, u, r ** Lv)
            elif pop == 'B':
                mod = QB * r ** Lv; res = 1
            elif pop == 'C':
                mod = QB * r; res = L.crt(1, QB, rng.choice(NR), r)
            else:
                mod, res = 24, 1
            p = prime_in(mod, res, lo)
            H = hits(p)
            assert H, p
            hM, hf, hP = min(H)
            assert L.es_solution(hf, hP, p) is not None
            best = min((escape(M, p), M, fam, P) for M, fam, P in H)
            E, EM, Ef, EP = best
            assert L.es_solution(Ef, EP, p) is not None
            fE = fac(E)
            single = len(fE) == 1 and list(fE.values())[0] == 1
            q = max(fE)
            v17 = sympy.multiplicity(17, EM)
            rows.append((hM, E, single, q, v17, p))
            print(f'B={B} {pop} p={p} h={hM} ({hf}{hP}) E={E} M={EM} ({Ef}{EP}) v17(M)={v17}', flush=True)
        hs = sorted(t[0] for t in rows); Es = sorted(t[1] for t in rows)
        sing = sum(t[2] and t[3] > B and t[3] != 17 for t in rows)
        at17 = sum(t[1] in (17, 289) for t in rows)
        qs = sorted({t[3] for t in rows if t[2]})
        ndist = len({t[5] for t in rows})
        print(f'SUMMARY B={B} {pop}: distinct primes {ndist}/{NP}; median h={hs[len(hs)//2]} median E={Es[len(Es)//2]} '
              f'E single prime q>B (q!=17): {sing}/{NP}; E a 17-power: {at17}/{NP}; '
              f'max v17(M of E-witness)={max(t[4] for t in rows)}; single-prime E values: {qs[:12]}', flush=True)
