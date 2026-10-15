# z11_pool.py — class pool for the exponent-tree covering of n_s = c0*4^s + k (input for z11_tree.c).
# HP = primes <= LMAXP with exponent caps; admissible odd prime powers q^e <= QMAX with ord_{q^e}(4) | H; moduli
# M = 2^a M' <= MMAX (M' from distinct admissible prime powers), period L_M = lcm ord <= LCAP.  For each period Lp the union
# E_Lp = {s mod Lp : n_s mod M in some class of modulus M, L_M = Lp} (s >= 4 representative), stored in mixed-radix
# index order idx(s) = sum_l (s mod l^f_l) * stride_l (l ascending).  Divisor classes D_q (q prime, q !| k) included.
# Output binary file (int64 little-endian): nHP, HP[], cap[], nper, then per period: f[nHP], Lp, bytes E (Lp, 0/1).
# Also writes <out>.moduli.json: Lp -> list of moduli (for witness recovery).
# Usage: PYTHONPATH=scripts uv run python scripts/z11_pool.py c0 k LMAXP QMAX MMAX LCAP out [caps l:e,...] [b=4]
import sys, time, json
from math import lcm
from collections import defaultdict
import numpy as np
from sympy import n_order, factorint, primerange
import mordell_lib as ML

c0, k, LMAXP, QMAX, MMAX, LCAP = map(int, sys.argv[1:7])
OUT = sys.argv[7]
CAP = {2: 8, 3: 6, 5: 4, 7: 3, 11: 2, 13: 2}
if len(sys.argv) > 8 and sys.argv[8] != '-':
    for t in sys.argv[8].split(','):
        a, b = t.split(':'); CAP[int(a)] = int(b)
HP = list(primerange(2, LMAXP + 1))
H = 1
for l in HP: H *= l ** CAP.get(l, 1)
t0 = time.time()
pps = []
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        if H % o or o > LCAP: break
        pps.append((q, Q, o))
        Q *= q
odd = [(1, 1)]
byq = defaultdict(list)
for q, Q, o in pps: byq[q].append((Q, o))
for q in sorted(byq):
    new = []
    for m, L in odd:
        for Q, o in byq[q]:
            if m * Q <= MMAX and lcm(L, o) <= LCAP: new.append((m * Q, lcm(L, o)))
    odd += new
print('prime powers %d, odd parts %d, %.1fs' % (len(pps), len(odd), time.time() - t0), flush=True)


def powers4(M, Lp):
    """4^(s + 4*Lp) mod M for s in range(Lp), as int64 array (M < 2^31)."""
    B = min(Lp, 4096)
    blk = np.empty(B, dtype=np.int64)
    x = pow(4, 4 * Lp, M)
    for i in range(B):
        blk[i] = x; x = x * 4 % M
    out = np.empty(Lp, dtype=np.int64)
    step = pow(4, B, M)
    cur = blk
    for st in range(0, Lp, B):
        n = min(B, Lp - st)
        out[st:st + n] = cur[:n]
        cur = cur * step % M
    return out


E = {}
mods = defaultdict(list)
nM = 0
for m, Lp in odd:
    for a in (0, 2, 3, 4, 5, 6, 7, 8):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        W = ML.residue_table(M)
        R = np.array(sorted(r for r in W if r % 2 ** a == k % 2 ** a), dtype=np.int64)
        if len(R) == 0: continue
        n = (c0 * powers4(M, Lp) + k) % M
        hit = np.isin(n, R)
        if hit.any():
            nM += 1
            mods[Lp].append(M)
            E[Lp] = E[Lp] | hit if Lp in E else hit
for q, Q, o in pps:
    if Q == q and k % q:
        hit = (c0 * powers4(q, o) + k) % q == 0
        if hit.any():
            mods[o].append(-q)
            E[o] = E[o] | hit if o in E else hit
print('moduli with hits %d, periods %d, total size %d, %.1fs' % (nM, len(E), sum(len(v) for v in E.values()),
                                                                 time.time() - t0), flush=True)
with open(OUT, 'wb') as fh:
    hdr = [len(HP)] + HP + [CAP.get(l, 1) for l in HP] + [len(E)]
    fh.write(np.array(hdr, dtype=np.int64).tobytes())
    for Lp in sorted(E):
        f = factorint(Lp)
        fv = [f.get(l, 0) for l in HP]
        s = np.arange(Lp, dtype=np.int64)
        idx = np.zeros(Lp, dtype=np.int64)
        stride = 1
        for l in HP:
            if fv[HP.index(l)]:
                rad = l ** fv[HP.index(l)]
                idx += (s % rad) * stride
                stride *= rad
        arr = np.zeros(Lp, dtype=np.uint8)
        arr[idx] = E[Lp].astype(np.uint8)
        fh.write(np.array(fv + [Lp], dtype=np.int64).tobytes())
        fh.write(arr.tobytes())
json.dump({str(Lp): v for Lp, v in mods.items()}, open(OUT + '.moduli.json', 'w'))
print('written', OUT, '%.1fs' % (time.time() - t0))
