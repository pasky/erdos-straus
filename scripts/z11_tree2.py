# z11_tree2.py — tree covering of the exponent space Zhat for n_s = c0*4^s + k, single-prime refinement steps.
# Node = residue u mod L (L | H, H = prod_{l <= LMAXP} l^cap_l).  Pool: ET classes / divisor classes of modulus
# M = 2^a M' <= MMAX, odd prime powers q^e <= QMAX with ord_{q^e}(4) | H; class period L_M = lcm ord.  A node is a leaf if
# some class with L_M | L contains n_u (n mod M depends only on u mod L_M for s >= 4).  Otherwise split L -> L*l for the
# prime l maximising the fraction of children that become leaves (fallback: two-prime steps, then the smallest prime).
# Writes a stream certificate for z11_check.py.
# Usage: PYTHONPATH=scripts uv run python scripts/z11_tree2.py c0 k LMAXP QMAX MMAX NODEMAX [out.json] [caps l:e,...]
import sys, json, time
from math import lcm
from collections import defaultdict
import numpy as np
from sympy import n_order, factorint, primerange
import mordell_lib as ML

c0, k, LMAXP, QMAX, MMAX, NODEMAX = map(int, sys.argv[1:7])
OUT = sys.argv[7] if len(sys.argv) > 7 and sys.argv[7] != '-' else None
CAP = {2: 8, 3: 6, 5: 4, 7: 3, 11: 2, 13: 2}
if len(sys.argv) > 8:
    for t in sys.argv[8].split(','):
        a, b = t.split(':'); CAP[int(a)] = int(b)
HP = list(primerange(2, LMAXP + 1))
cap = np.array([CAP.get(l, 1) for l in HP])
H = 1
for l, e in zip(HP, cap): H *= l ** int(e)
pidx = {l: i for i, l in enumerate(HP)}
t0 = time.time()


def evec(x):
    v = np.zeros(len(HP), dtype=np.int64)
    for l, e in factorint(x).items(): v[pidx[l]] = e
    return v


pps = []
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        if H % o: break
        pps.append((q, Q, o))
        Q *= q
odd = [(1, 1)]
byq = defaultdict(list)
for q, Q, o in pps: byq[q].append((Q, o))
for q in sorted(byq):
    new = []
    for m, L in odd:
        for Q, o in byq[q]:
            if m * Q <= MMAX: new.append((m * Q, lcm(L, o)))
    odd += new
byper = defaultdict(list)  # Lp -> [(M, {r: cls})]
nres = 0
for m, Lp in odd:
    for a in (0, 2, 3, 4, 5, 6, 7, 8):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        W = ML.residue_table(M)
        W = {r: c for r, c in W.items() if r % 2 ** a == k % 2 ** a}
        if W: byper[Lp].append((M, W)); nres += len(W)
for q, Q, o in pps:
    if Q == q and k % q: byper[o].append((q, {0: ('D', (q,))}))
plist = sorted(byper)
PE = np.array([evec(Lp) for Lp in plist])
print('prime powers %d, moduli %d, residues %d, periods %d, H=%d, %.1fs' % (
    len(pps), sum(len(v) for v in byper.values()), nres, len(plist), H, time.time() - t0), flush=True)
memo = {}
dbgc = []
DBG = int(__import__('os').environ.get('DBG', '0'))


def cover(i, x):
    """witness class of period plist[i] containing exponent residue x mod plist[i] (or None)"""
    key = (i, x)
    if key in memo: return memo[key]
    Lp = plist[i]
    S = x + 4 * Lp
    w = None
    for M, W in byper[Lp]:
        r = (c0 * pow(4, S, M) + k) % M
        if r in W:
            w = (M, r, W[r]); break
    memo[key] = w
    return w


def leaf(le, u, mask=None):
    sel = (PE <= le).all(1)
    if mask is not None: sel &= ~mask
    for i in np.nonzero(sel)[0]:
        w = cover(i, u % plist[i])
        if w: return w
    return None


stream = []
nodes = 0
stuck = []
maxL = 1


def split_score(L, le, u, steps):
    te = le.copy()
    for l in steps: te[pidx[l]] += 1
    if (te > cap).any(): return None
    g = 1
    for l in steps: g *= l
    old = (PE <= le).all(1)
    new = np.nonzero((PE <= te).all(1) & ~old)[0]
    if len(new) == 0: return 0, g
    c = 0
    for j in range(g):
        x = u + j * L
        for i in new:
            if cover(i, x % plist[i]):
                c += 1; break
    return c, g


def solve(L, le, u):
    global nodes, maxL
    nodes += 1
    maxL = max(maxL, L)
    if nodes > NODEMAX: raise RuntimeError('node budget')
    w = leaf(le, u)
    if w:
        stream.append(('C', w[0], w[1], w[2][0], list(w[2][1]))); return
    best = None
    for l in HP:
        s = split_score(L, le, u, [l])
        if s and s[0] and (best is None or s[0] / s[1] > best[0]): best = (s[0] / s[1], [l])
    if best is None:
        for a in range(len(HP)):
            for b in range(a, len(HP)):
                if HP[a] * HP[b] > 400: continue
                s = split_score(L, le, u, [HP[a], HP[b]])
                if s and s[0] and (best is None or s[0] / s[1] > best[0]): best = (s[0] / s[1], [HP[a], HP[b]])
    if best is None:
        free = [l for l in HP if le[pidx[l]] < cap[pidx[l]]]
        if not free:
            stuck.append((L, u)); stream.append(('X',)); return
        best = (0, [min(free, key=lambda l: l ** (int(le[pidx[l]]) + 1))])
    if DBG and len(stream) < 10**9 and dbgc.append(1) is None and len(dbgc) <= DBG: print('node', nodes, dict((l, int(e)) for l, e in zip(HP, le) if e), u % L, '->', best, flush=True)
    te = le.copy()
    g = 1
    for l in best[1]: te[pidx[l]] += 1; g *= l
    T = L * g
    stream.append(('S', T))
    for j in range(g):
        solve(T, te, u + j * L)


sys.setrecursionlimit(100000)
try:
    L0 = int(__import__('os').environ.get('L0', '1'))
    if L0 > 1:
        stream.append(('S', L0))
        for j in range(L0): solve(L0, evec(L0), j)
    else:
        solve(1, np.zeros(len(HP), dtype=np.int64), 0)
    ok = not stuck
except RuntimeError as e:
    ok = False
    print('ABORT', e)
nleaf = sum(1 for x in stream if x[0] == 'C')
print('nodes %d leaves %d stuck %d maxL %d ok=%s %.1fs' % (nodes, nleaf, len(stuck), maxL, ok, time.time() - t0))
if stuck: print('stuck (L,u):', stuck[:10])
if ok and OUT:
    json.dump({'c0': c0, 'k': k, 'stream': stream}, open(OUT, 'w'))
    print('written', OUT, 'distinct classes', len({(x[1], x[2]) for x in stream if x[0] == 'C'}))
