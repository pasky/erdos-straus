"""Hybrid adaptive covering search (task O103): m13c_dfs (brute-force tables M <= Mmax for the choice of
the split) + the complete C witness engine m13d_wit.c at every node (all ET classes with M | L, any size).

usage: m13d_dfs.py roots Mmax Pmax emax maxnodes maxsec out.json
  roots: comma list x:L.  A popped node x mod L is first tested by the complete engine (with req = the
  full power of the last split prime: classes with M | L_parent were already excluded at the parent);
  if covered -> leaf; else split at the prime (new prime <= Pmax, or one more power, exponent caps as
  in m13c_dfs) minimising the fraction of children not covered by tables M <= Mmax.  Table-covered
  children become leaves at once; the others are pushed (largest mass first).
  When maxnodes or maxsec is exceeded, the remaining queue is marked open.  Output format = m13c_dfs.
"""
import sys, json, time, heapq, os, gzip
import numpy as np
import mordell_dfs as D
from mordell_cover import primes_upto
from m13d_wit import Engine


def modres(fam, P, x):
    a, b, c = P
    if fam in ('I2', 'I3', 'II3'):
        M = 4 * a * b * c
    elif fam == 'II2':
        M = c
    else:
        M = 4 * a * b
    return M, x % M


def main():
    roots = [tuple(map(int, s.split(':'))) for s in sys.argv[1].split(',')]
    Mmax = int(sys.argv[2]); Pmax = int(sys.argv[3]); emax = int(sys.argv[4])
    maxnodes = int(sys.argv[5]); maxsec = float(sys.argv[6]); out = sys.argv[7]
    D.BOUND[0] = Mmax
    PR = primes_upto(Pmax)
    E = Engine()
    t0 = time.time()
    tree = {'r': 13, 'variant': 'main', 'Mmax': Mmax, 'engine': 'm13d_wit', 'roots': []}
    heap = []; cnt = 0; nodes = 0; nC = 0; open_leaves = []; openmass = 0.0; cw = 0
    for x, L in roots:
        rec = {'x': x, 'L': L}
        tree['roots'].append(rec)
        heapq.heappush(heap, (-1.0 / len(roots), cnt, L, x, 1, rec)); cnt += 1
    stop = False
    while heap:
        negm, _, L, x, req, rec = heapq.heappop(heap)
        mass = -negm
        nodes += 1
        if not stop and (nodes > maxnodes or time.time() - t0 > maxsec):
            stop = True
        if stop:
            rec['open'] = True; open_leaves.append((L, x, mass)); openmass += mass
            continue
        w = E.query(x, L, req)
        if w:
            fam, P = w[0]
            M, r = modres(fam, P, x)
            rec['leaf'] = [M, r, fam, list(P)]; cw += 1
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
        rq = p
        while L2 % (rq * p) == 0:
            rq *= p
        rec['split'] = p; rec['children'] = []
        for y, c in zip(Y, cov.tolist()):
            y %= L2
            ch = {'x': y, 'L': L2}
            rec['children'].append(ch)
            if not c:
                heapq.heappush(heap, (-mass / len(Y), cnt, L2, y, rq, ch)); cnt += 1
            else:
                M, res, (fam, P) = D.witness(y, L2, Mmax)
                ch['leaf'] = [M, res, fam, list(P)]
        if nodes % 200 == 0:
            om = sum(-s[0] for s in heap)
            print(f"nodes={nodes} queue={len(heap)} openmass={om:.3e} Cwit={cw} split={p} "
                  f"surv={int((~cov).sum())}/{len(Y)} t={time.time()-t0:.0f}s", flush=True)
    print(f"done nodes={nodes} open={len(open_leaves)} openmass={openmass:.4e} Cwit={cw} t={time.time()-t0:.0f}s")
    for L, x, m in sorted(open_leaves, key=lambda z: -z[2])[:10]:
        print("open", x, L, f"{m:.2e}")
    json.dump(tree, (gzip.open if out.endswith('.gz') else open)(out, 'wt'))


if __name__ == '__main__':
    main()
