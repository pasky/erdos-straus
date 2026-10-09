"""Adaptive covering search (mordell_dfs engine) started from explicit roots (task O100).

usage: m13c_dfs.py roots Mmax Pmax emax maxnodes [out.json]
  roots: comma list x:L (e.g. 112561:720720). Brute-force classes M | L, M <= Mmax.
  Writes a tree certificate (same format as mordell_dfs.py, 'roots' with x, L) and prints open leaves.
"""
import sys, json, time, heapq, os
import numpy as np
import mordell_lib
import mordell_dfs as D
from mordell_cover import primes_upto
mordell_lib.I1_CAP[0] = int(float(os.environ.get('MORDELL_I1CAP', '0')))

def main():
    roots = [tuple(map(int, s.split(':'))) for s in sys.argv[1].split(',')]
    Mmax = int(sys.argv[2]); Pmax = int(sys.argv[3]); emax = int(sys.argv[4]); maxnodes = int(sys.argv[5])
    out = sys.argv[6] if len(sys.argv) > 6 else None
    D.BOUND[0] = Mmax
    PR = primes_upto(Pmax)
    t0 = time.time()
    tree = {'r': 13, 'variant': 'main', 'Mmax': Mmax, 'roots': []}
    stack = []; cnt = 0; nodes = 0; open_leaves = []; openmass = 0.0
    for x, L in roots:
        rec = {'x': x, 'L': L}
        tree['roots'].append(rec)
        heapq.heappush(stack, (-1.0 / len(roots), cnt, L, x, rec)); cnt += 1
    while stack:
        negm, _, L, x, rec = heapq.heappop(stack)
        mass = -negm
        nodes += 1
        if nodes > maxnodes:
            rec['open'] = True; open_leaves.append((L, x, mass)); openmass += mass
            continue
        wv = D.witness(x, L, Mmax)
        if wv is not None:
            M, res, (fam, P) = wv
            rec['leaf'] = [M, res, fam, list(P)]
            continue
        best = None
        for p in PR:
            if L % p == 0:
                e = 0
                while L % p ** (e + 1) == 0:
                    e += 1
                if e >= (emax + 3 if p == 2 else emax + 1 if p == 3 else emax):
                    continue
                q = p ** (e + 1)
            else:
                q = p
            mods, L2 = D.new_moduli(L, q, p, Mmax)
            t = np.arange(p, dtype=np.int64)
            T = t[(x % p + (L % p) * t) % p != 0]
            cov = D.covered_by(x, L, T, mods)
            ns = int((~cov).sum())
            score = ns / len(T)
            if best is None or score < best[0]:
                best = (score, p, L2, [x + L * int(tt) for tt in T], cov)
            if ns == 0:
                break
        if best is None:
            rec['open'] = True; open_leaves.append((L, x, mass)); openmass += mass
            continue
        score, p, L2, Y, cov = best
        rec['split'] = p; rec['children'] = []
        for y, c in zip(Y, cov.tolist()):
            ch = {'x': y, 'L': L2}
            rec['children'].append(ch)
            if not c:
                heapq.heappush(stack, (-mass / len(Y), cnt, L2, y, ch)); cnt += 1
            else:
                M, res, (fam, P) = D.witness(y, L2, Mmax)
                ch['leaf'] = [M, res, fam, list(P)]
        if nodes % 200 == 0:
            om = sum(-s[0] for s in stack)
            print(f"nodes={nodes} queue={len(stack)} openmass={om:.3e} split={p} surv={int((~cov).sum())}/{len(Y)} t={time.time()-t0:.0f}s", flush=True)
    print(f"done nodes={nodes} open={len(open_leaves)} openmass={openmass:.4e} t={time.time()-t0:.0f}s")
    for L, x, m in sorted(open_leaves, key=lambda z: -z[2])[:10]:
        print("open", x, L, f"{m:.2e}")
    if out:
        json.dump(tree, open(out, 'w'))

if __name__ == '__main__':
    main()
