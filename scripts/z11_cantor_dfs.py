# z11_cantor_dfs.py — DFS version of z11_cantor.py: cover the "label Cantor set" C = prod_l LABELS (each l-adic component
# of the exponent equal to one of the integer square points, e.g. 4, -2, 2, 3 for k = 105) by ET/divisor classes.
# Primes l are assigned in increasing order; a prefix pattern survives if no class whose period support lies in the
# assigned primes contains it.  Prints the survivors per prime.  On C the l-adic components are exact, so a class meets C in
# a cylinder over supp(L_M) (exponents of l irrelevant).
# Usage: PYTHONPATH=scripts uv run python scripts/z11_cantor_dfs.py c0 k LMAX QMAX MMAX LABELS [maxsurv]
import sys, time
from collections import defaultdict
from sympy import n_order, factorint, primerange
from sympy.ntheory.modular import crt
import mordell_lib as ML

c0, k, LMAX, QMAX, MMAX = map(int, sys.argv[1:6])
LAB = [int(x) for x in sys.argv[6].split(',')]
MAXS = int(sys.argv[7]) if len(sys.argv) > 7 else 10 ** 6
S = list(primerange(2, LMAX + 1))
t0 = time.time()
pps = []
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        f = factorint(o)
        if any(l > LMAX for l in f): break
        pps.append((q, Q, f))
        Q *= q
odd = [(1, (), frozenset())]
byq = defaultdict(list)
for q, Q, f in pps: byq[q].append((Q, f))
for q in sorted(byq):
    new = []
    for m, parts, sp in odd:
        for Q, f in byq[q]:
            if m * Q <= MMAX: new.append((m * Q, parts + ((Q, f),), sp | frozenset(f)))
    odd += new
bymax = defaultdict(list)  # max support prime -> [(M, a, parts, support)]
for m, parts, sp in odd:
    for a in (0, 2, 3, 4, 5, 6, 7):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        bymax[max(sp) if sp else 1].append((M, a, parts, sp))
for q, Q, f in pps:
    if Q == q and k % q: bymax[max(f) if f else 1].append((q, -1, ((q, f),), frozenset(f)))
print('S up to %d, prime powers %d, moduli %d, %.1fs' % (LMAX, len(pps), sum(map(len, bymax.values())), time.time() - t0),
      flush=True)
WC = {}


def W(M):
    if M not in WC: WC[M] = ML.residue_table(M)
    return WC[M]


def value(M, a, parts, pat):
    ms, rs = ([2 ** a], [k % 2 ** a]) if a > 0 else ([], [])
    for Q, f in parts:
        mods = [l ** e for l, e in f.items()]
        mu = int(crt(mods, [LAB[pat[l]] % (l ** e) for l, e in f.items()])[0]) if mods else 0
        ms.append(Q); rs.append((c0 * pow(4, mu, Q) + k) % Q)
    return int(crt(ms, rs)[0])


def hit(pat, cls):
    M, a, parts, sp = cls
    r = value(M, a, parts, pat)
    if a == -1: return (M, 'D') if r == 0 else None
    w = W(M).get(r)
    return (M, w) if w else None


surv = [dict()]
# classes with empty support (constant value): check once
for cls in bymax.get(1, []):
    if hit({}, cls): print('a constant class covers everything:', cls[0]); surv = []; break
for l in S:
    new = []
    for pat in surv:
        for v in range(len(LAB)):
            p2 = dict(pat); p2[l] = v
            if not any(hit(p2, cls) for cls in bymax.get(l, [])): new.append(p2)
    surv = new
    print('after l=%d: %d survivors %.1fs' % (l, len(surv), time.time() - t0), flush=True)
    for p in surv[:4]: print('   ', ' '.join('%d:%d' % (x, LAB[p[x]]) for x in sorted(p)))
    if not surv or len(surv) > MAXS: break
