# z11_tree.py — per-branch ("tree") exponent covering of n_s = c0*4^s + k by ET classes and divisor classes.
# Exponent space Zhat; a node is a residue u mod L (L | H).  Pool: every class whose modulus M = 2^a * M' has M' built from
# odd prime powers q^e <= QMAX with ord_{q^e}(4) | H, M <= MMAX, period L_M <= LCAP.  Each pool class pulls back to a set
# E_M of exponent residues mod L_M.  Node (L,u) is a leaf if some class with L_M | L contains u; otherwise it is split to
# T = lcm(L, L_p) for the period L_p (in the pool) whose union set covers the largest fraction of the lifts of u.
# Output (optional): stream certificate for z11_check.py.
# Usage: PYTHONPATH=scripts uv run python scripts/z11_tree.py c0 k H QMAX MMAX LCAP NODEMAX [out.json]
import sys, json, time, functools
from math import gcd, lcm
from collections import defaultdict
from sympy import n_order, factorint, primerange
import mordell_lib as ML
import numpy as np

c0, k, H, QMAX, MMAX, LCAP, NODEMAX = map(int, sys.argv[1:8])
OUT = sys.argv[8] if len(sys.argv) > 8 else None
GMAX = int(__import__('os').environ.get('GMAX', '64'))
t0 = time.time()


def LMof(M):
    out = 1
    for q, e in factorint(M).items():
        if q != 2: out = lcm(out, n_order(4, q ** e))
    return out


# admissible odd prime powers
pps = []  # (q, Q, ordQ)
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    o = n_order(4, q)
    if H % o: continue
    Q = q
    while Q <= QMAX:
        oQ = n_order(4, Q)
        if H % oQ: break
        pps.append((q, Q, oQ))
        Q *= q
print('admissible prime powers:', len(pps), [Q for _, Q, _ in pps][:40], flush=True)

# odd parts M' (products of admissible prime powers of distinct primes)
odd = [(1, 1)]  # (M', L)
byq = defaultdict(list)
for q, Q, o in pps: byq[q].append((Q, o))
for q in sorted(byq):
    new = []
    for m, L in odd:
        for Q, o in byq[q]:
            if m * Q <= MMAX and lcm(L, o) <= LCAP: new.append((m * Q, lcm(L, o)))
    odd += new
print('odd parts:', len(odd), flush=True)

# period -> {s mod Lp: (M, r, cls)}
per = defaultdict(dict)
ncls = 0
for m, L in odd:
    if L > LCAP: continue
    for a in (0, 2, 3, 4, 5, 6, 7, 8):
        M = (2 ** a) * m
        if M > MMAX or M < 3: continue
        if a == 0 and M % 4 != 3: continue
        W = ML.residue_table(M) if (a > 0 or M % 4 == 3) else {}
        W = {r: c for r, c in W.items() if r % (2 ** a) == k % (2 ** a)}
        if not W: continue
        S0 = L * ((a + 1) // 2 // L + 1)
        y = pow(4, S0, M)
        d = per[L]
        hit = False
        for s in range(L):
            r = (c0 * y + k) % M
            if r in W and s not in d:
                d[s] = (M, r, W[r]); hit = True
            y = y * 4 % M
        ncls += hit
# divisor classes
for q, Q, o in pps:
    if Q != q or k % q == 0: continue
    d = per[o]
    y = 1
    for s in range(o):
        if (c0 * y + k) % q == 0 and s not in d: d[s] = (q, 0, ('D', (q,)))
        y = y * 4 % q
per = {Lp: d for Lp, d in per.items() if d}
plist = sorted(per)
print('moduli with hits: %d, periods: %d, total residues %d, %.1fs' % (ncls, len(plist), sum(len(d) for d in per.values()),
                                                                   time.time() - t0), flush=True)


HP = sorted(factorint(H))
hexp = np.array([factorint(H)[l] for l in HP])


def evec(x):
    f = factorint(x)
    return np.array([f.get(l, 0) for l in HP])


PE = np.array([evec(Lp) for Lp in plist])
parr = plist


def leafclass(L, u):
    for Lp in plist:
        if L % Lp == 0:
            w = per[Lp].get(u % Lp)
            if w: return (Lp, w)
    return None


stream = []  # ('S', T) / ('C', M, r, fam, P) in DFS order
nodes = 0
stuck = []


def best_split(L, u):
    le = evec(L)
    divL = (PE <= le).all(1)
    best = None
    seen = set()
    for i in np.nonzero(~divL)[0]:
        te = np.maximum(le, PE[i])
        if (te > hexp).any(): continue
        tk = tuple(te)
        if tk in seen: continue
        seen.add(tk)
        T = 1
        for l, e in zip(HP, te): T *= l ** int(e)
        g = T // L
        if g > GMAX: continue
        newp = [parr[j] for j in np.nonzero((PE <= te).all(1) & ~divL)[0]]
        c = 0
        for j in range(g):
            x = u + j * L
            if any(x % Lp in per[Lp] for Lp in newp): c += 1
        if not c: continue
        key = (c / g, -g)
        if best is None or key > best[0]: best = (key, T)
    return best


sys.setrecursionlimit(10000)
maxL = 1


def solve(L, u, depth):
    global nodes, maxL
    nodes += 1
    maxL = max(maxL, L)
    if nodes > NODEMAX: raise RuntimeError('node budget')
    w = leafclass(L, u)
    if w:
        M, r, (fam, P) = w[1]
        stream.append(('C', M, r, fam, list(P)))
        return
    b = best_split(L, u)
    if b is None:
        # no class in the pool meets the lifts: refine by the smallest prime with L*l | H
        for l in sorted(factorint(H)):
            if H % (L * l) == 0:
                T = L * l; break
        else:
            stuck.append((L, u)); stream.append(('X',)); return
    else:
        T = b[1]
    stream.append(('S', T))
    for j in range(T // L):
        solve(T, u + j * L, depth + 1)


try:
    solve(1, 0, 0)
    ok = not stuck
except RuntimeError as e:
    ok = False
    print('ABORT', e)
nleaf = sum(1 for x in stream if x[0] == 'C')
print('nodes %d leaves %d stuck %d maxL %d ok=%s %.1fs' % (nodes, nleaf, len(stuck), maxL, ok, time.time() - t0))
if stuck: print('stuck nodes (L,u):', stuck[:20])
if ok and OUT:
    json.dump({'c0': c0, 'k': k, 'stream': stream}, open(OUT, 'w'))
    print('written', OUT)
