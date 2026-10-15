# z11_line.py — cover an l-line through an integer point x of the exponent space of n_s = c0*4^s + k:
# X = {mu : mu_l' = x for every prime l' != l, mu_l = c in Z_l free}.  Every class (any modulus M = 2^a M' <= MMAX, odd prime
# powers <= QMAX, any order) meets X in a union of classes c mod l^v, v = v_l(L_M) (other components are exact).
# Reports the residues c mod l^e (e <= E) not covered by any class with v <= e.  (Optionally a second free prime l2:c2
# fixed: mu_l2 = c2 exactly.)
# Usage: PYTHONPATH=scripts uv run python scripts/z11_line.py c0 k x l E QMAX MMAX [l2:c2 ...]
import sys, time
from collections import defaultdict
from sympy import n_order, factorint, primerange
from sympy.ntheory.modular import crt
import mordell_lib as ML

c0, k, X, ELL, E, QMAX, MMAX = map(int, sys.argv[1:8])
FIX = {int(a.split(':')[0]): int(a.split(':')[1]) for a in sys.argv[8:]}
t0 = time.time()
pps = []
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        f = factorint(o)
        if f.get(ELL, 0) > E: break
        pps.append((q, Q, f))
        Q *= q


def comp_mod(f, c):
    """mu mod ord for the point with mu_ELL = c, mu_l2 = FIX, else X"""
    ms, rs = [], []
    for l, e in f.items():
        ms.append(l ** e)
        rs.append((c if l == ELL else FIX.get(l, X)) % l ** e)
    return int(crt(ms, rs)[0]) if ms else 0


cov = [set() for _ in range(E + 1)]  # cov[v] = covered residues mod ELL^v
wit = {}
byq = defaultdict(list)
for q, Q, f in pps: byq[q].append((Q, f))
odd = [(1, ())]
for q in sorted(byq):
    new = []
    for m, parts in odd:
        for Q, f in byq[q]:
            if m * Q <= MMAX: new.append((m * Q, parts + ((Q, f),)))
    odd += new
print('prime powers %d, odd parts %d, %.1fs' % (len(pps), len(odd), time.time() - t0), flush=True)
for m, parts in odd:
    v = max([f.get(ELL, 0) for Q, f in parts] + [0])
    for a in (0, 2, 3, 4, 5, 6, 7):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        W = ML.residue_table(M)
        if not W: continue
        for c in range(ELL ** v):
            if c in cov[v]: continue
            ms, rs = ([2 ** a], [k % 2 ** a]) if a else ([], [])
            for Q, f in parts:
                ms.append(Q); rs.append((c0 * pow(4, comp_mod(f, c), Q) + k) % Q)
            r = int(crt(ms, rs)[0])
            if r in W:
                cov[v].add(c); wit[(v, c)] = (M, W[r])
for q, Q, f in pps:
    if Q == q and k % q:
        v = f.get(ELL, 0)
        for c in range(ELL ** v):
            if c not in cov[v] and (c0 * pow(4, comp_mod(f, c), q) + k) % q == 0:
                cov[v].add(c); wit[(v, c)] = (q, 'D')
unc = [0]
for e in range(E + 1):
    if e > 0: unc = [u + j * ELL ** (e - 1) for u in unc for j in range(ELL)]
    unc = [u for u in unc if not any((u % ELL ** v) in cov[v] for v in range(e + 1))]
    print('precision %d^%d: %d uncovered %s' % (ELL, e, len(unc), unc[:20]))
print('classes used at v=0:', [wit[(0, 0)]] if (0, 0) in wit else 'none (the point x itself is not covered at level 0)')
print('%.1fs' % (time.time() - t0))
