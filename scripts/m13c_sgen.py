"""S-generic points of open tree leaves (task O100 §8).
For an open leaf (x mod L), S = primes of L, its S-generic point P has P_q = x (the integer) for q in S and
P_q = 1 for q not in S.  A class n = r (mod M) contains P iff r = x (mod M_S) and r = 1 (mod M/M_S), M_S = S-part.
usage: m13c_sgen.py Mmax tree.json.gz root [cache.npz]   — tests every open leaf of the root against all
classes with M <= Mmax (brute-force mordell_lib tables), prints the uncovered S-generic points."""
import sys, json, gzip, os, time
import numpy as np
from mordell_lib import iter_classes, cls_modulus_residues
Mmax = int(sys.argv[1]); root = int(sys.argv[3])
cache = sys.argv[4] if len(sys.argv) > 4 else f"/tmp/o100/cls_{Mmax}.npz"
if os.path.exists(cache):
    z = np.load(cache); Ms, Rs = z['M'], z['R']
else:
    t0 = time.time(); Ml, Rl = [], []
    for M in range(3, Mmax + 1):
        S = set()
        for fam, P in iter_classes(M):
            S.update(cls_modulus_residues(fam, P)[1])
        Ml += [M] * len(S); Rl += sorted(S)
    Ms, Rs = np.array(Ml, dtype=np.int64), np.array(Rl, dtype=np.int64)
    np.savez(cache, M=Ms, R=Rs); print(f"built {len(Ms)} residues in {time.time()-t0:.0f}s", flush=True)
T = json.load(gzip.open(sys.argv[2], 'rt'))
rt = [r for r in T['roots'] if r['x'] == root][0]
opens = []; st = [rt]
while st:
    nd = st.pop()
    if 'children' in nd: st += nd['children']
    elif nd.get('open'): opens.append((nd['x'], nd['L']))
if os.environ.get('LEAVES'):
    opens = [tuple(map(int, t.split(':'))) for t in os.environ['LEAVES'].split(',')]
unc = []
for x, L in opens:
    g = np.gcd(Ms, L)
    for _ in range(6):
        g = np.gcd(Ms, g * g)
    N = Ms // g
    ok = ((Rs - 1) % N == 0) & ((Rs - x) % g == 0)
    if not ok.any():
        unc.append((x, L))
    elif os.environ.get('LEAVES'):
        i = int(np.nonzero(ok)[0][0]); print('covered', x, L, 'by M =', Ms[i], 'r =', Rs[i])
print(f"root {root}: {len(opens)} open leaves, S-generic point uncovered (M<={Mmax}) for {len(unc)}")
for x, L in unc[:20]:
    print("UNC", x, L)
