# z11_cantor_tree.py — adaptive tree covering of the label Cantor set C = prod_l LABELS (see z11_cantor_dfs.py).
# A node is a finite assignment A (prime l -> label).  For each candidate prime l not in A, count the labels v for which
# some class with period support in dom(A) + {l}, containing l, contains the point; branch on the l with the most such
# labels (all labels killed = node closed).  Prints the tree size and the open nodes left at the depth limit.
# Usage: PYTHONPATH=scripts uv run python scripts/z11_cantor_tree.py c0 k LMAX QMAX MMAX LABELS [NODEMAX] [out.json]
import sys, time, json
from collections import defaultdict
from sympy import n_order, factorint, primerange
from sympy.ntheory.modular import crt
import mordell_lib as ML

c0, k, LMAX, QMAX, MMAX = map(int, sys.argv[1:6])
LAB = [int(x) for x in sys.argv[6].split(',')]
NODEMAX = int(sys.argv[7]) if len(sys.argv) > 7 else 10 ** 5
OUT = sys.argv[8] if len(sys.argv) > 8 else None
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
bysp = defaultdict(list)  # support -> classes
for m, parts, sp in odd:
    for a in (0, 2, 3, 4, 5, 6, 7):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        bysp[sp].append((M, a, parts))
for q, Q, f in pps:
    if Q == q and k % q: bysp[frozenset(f)].append((q, -1, ((q, f),)))
byl = defaultdict(list)  # l -> supports containing l
for sp in bysp:
    for l in sp: byl[l].append(sp)
print('prime powers %d, moduli %d, supports %d, %.1fs' % (len(pps), sum(map(len, bysp.values())), len(bysp),
                                                          time.time() - t0), flush=True)
WC = {}


def W(M):
    if M not in WC: WC[M] = ML.residue_table(M)
    return WC[M]


def hit(pat, cls):
    M, a, parts = cls
    ms, rs = ([2 ** a], [k % 2 ** a]) if a > 0 else ([], [])
    for Q, f in parts:
        mods = [l ** e for l, e in f.items()]
        mu = int(crt(mods, [LAB[pat[l]] % (l ** e) for l, e in f.items()])[0]) if mods else 0
        ms.append(Q); rs.append((c0 * pow(4, mu, Q) + k) % Q)
    r = int(crt(ms, rs)[0])
    if a == -1: return (M, 0, 'D', [M]) if r == 0 else None
    w = W(M).get(r)
    return (M, r, w[0], list(w[1])) if w else None


SPM = {}
SPL = {sp: tuple(sorted(sp)) for sp in bysp}


def sphit(sp, pat):
    key = (sp, tuple(pat[l] for l in SPL[sp]))
    if key not in SPM:
        w = None
        for cls in bysp[sp]:
            w = hit(pat, cls)
            if w: break
        SPM[key] = w
    return SPM[key]


def kills(A, l):
    dom = set(A) | {l}
    sps = [sp for sp in byl.get(l, []) if sp <= dom]
    out = {}
    for v in range(len(LAB)):
        p2 = dict(A); p2[l] = v
        for sp in sps:
            h = sphit(sp, p2)
            if h: out[v] = h; break
    return out


nodes = 0
openn = []
tree = []  # stream: ('B', l) branch / ('K', v, witness) killed label / ('O',) open


def solve(A, depth):
    global nodes
    nodes += 1
    if nodes % 100 == 0: print('nodes', nodes, 'depth', depth, 'open', len(openn), '%.0fs' % (time.time() - t0), flush=True)
    if nodes > NODEMAX: raise RuntimeError('budget')
    best = None
    for l in S:
        if l in A: continue
        kl = kills(A, l)
        if best is None or len(kl) > len(best[1]): best = (l, kl)
        if len(kl) == len(LAB): break
    l, kl = best
    if not kl:
        openn.append(dict(A)); tree.append(('O',)); return
    tree.append(('B', l))
    for v in range(len(LAB)):
        if v in kl:
            tree.append(('K', v, kl[v]))
        else:
            A2 = dict(A); A2[l] = v
            solve(A2, depth + 1)


try:
    solve({}, 0)
    print('DONE nodes %d open %d %.1fs' % (nodes, len(openn), time.time() - t0))
except RuntimeError:
    print('BUDGET nodes %d open %d %.1fs' % (nodes, len(openn), time.time() - t0))
for A in openn[:10]:
    print('  open:', ' '.join('%d:%d' % (x, LAB[A[x]]) for x in sorted(A)))
if OUT and not openn:
    json.dump({'c0': c0, 'k': k, 'labels': LAB, 'tree': tree}, open(OUT, 'w'))
    print('written', OUT, 'distinct classes', len({(t[2][0], t[2][1]) for t in tree if t[0] == 'K'}))
