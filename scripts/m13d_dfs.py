"""Hybrid adaptive covering search (task O103): m13c_dfs (brute-force tables M <= Mmax for the choice of
the split) + the complete C witness engine m13d_wit.c at every node (all ET classes with M | L, any size).

usage: m13d_dfs.py roots Mmax Pmax emax maxnodes maxsec out.json [CK]
  roots: comma list x:L.  A popped node x mod L is first tested by the complete engine (with req = the
  full power of the last split prime: classes with M | L_parent were already excluded at the parent);
  if covered -> leaf; else split at the prime (new prime <= Pmax, or one more power, exponent caps as
  in m13c_dfs) minimising the fraction of children not covered by tables M <= Mmax.  Table-covered
  children become leaves at once; the others are pushed (largest mass first).
  CK > 0: the CK candidate splits with fewest table survivors are scored by the complete engine
  (number of children open w.r.t. all classes M | L*q); the split minimising (#open, p) is taken.
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


CK = 0
# per-prime exponent caps (env M13D_CAPS='2:12,3:8') and primes always C-scored (env M13D_PRIO='2,3')
CAPS = {int(a): int(b) for a, b in (t.split(':') for t in os.environ.get('M13D_CAPS', '').split(',') if t)}
PRIO = {int(t) for t in os.environ.get('M13D_PRIO', '').split(',') if t}
STATS = open(os.environ['M13D_STATS'], 'w') if os.environ.get('M13D_STATS') else None


def main():
    roots = [tuple(map(int, s.split(':'))) for s in sys.argv[1].split(',')]
    Mmax = int(sys.argv[2]); Pmax = int(sys.argv[3]); emax = int(sys.argv[4])
    maxnodes = int(sys.argv[5]); maxsec = float(sys.argv[6]); out = sys.argv[7]
    global CK
    CK = int(sys.argv[8]) if len(sys.argv) > 8 else 0
    nC = [0]
    D.BOUND[0] = Mmax
    PR = primes_upto(Pmax)
    E = Engine()
    t0 = time.time()
    tree = {'r': 13, 'variant': 'main', 'Mmax': Mmax, 'engine': 'm13d_wit', 'roots': []}
    heap = []; cnt = 0; nodes = 0; open_leaves = []; openmass = 0.0; cw = 0
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
        w = E.query(x, L, req) if req > 0 else None
        if w:
            fam, P = w[0]
            M, r = modres(fam, P, x)
            rec['leaf'] = [M, r, fam, list(P)]; cw += 1
            continue
        cands = []
        for p in PR:
            if L % p == 0:
                e = 0
                while L % p ** (e + 1) == 0:
                    e += 1
                if e >= CAPS.get(p, emax + 3 if p == 2 else emax + 1 if p == 3 else emax):
                    continue
                q = p ** (e + 1)
            else:
                q = p
            mods, L2 = D.new_moduli(L, q, p, Mmax)
            t = np.arange(p, dtype=np.int64)
            T = t[(x % p + (L % p) * t) % p != 0]
            cov = D.covered_by(x, L, T, mods)
            ns = int((~cov).sum())
            cands.append((ns / len(T), ns, p, L2, [(x + L * int(tt)) % L2 for tt in T], cov.tolist()))
            if ns == 0 and CK == 0:
                break
        if not cands:
            rec['open'] = True; open_leaves.append((L, x, mass)); openmass += mass
            continue
        if CK == 0:
            score, ns, p, L2, Y, cov = min(cands, key=lambda c: c[0])
            wit = [None] * len(Y)
        else:
            # C-scored: evaluate the CK candidates with fewest table survivors; children found open by
            # the complete engine are counted; choose min (#open children, p).
            cands.sort(key=lambda c: (c[2] not in PRIO, c[1], c[2]))
            npr = sum(1 for c in cands if c[2] in PRIO)
            best = None
            for score, ns, p, L2, Y, cov in cands[:CK + npr]:
                rq = p
                while L2 % (rq * p) == 0:
                    rq *= p
                wit = []; nop = 0
                for y, c in zip(Y, cov):
                    if c:
                        wit.append(None); continue
                    w = E.query(y, L2, rq); nC[0] += 1
                    wit.append(w[0] if w else False); nop += not w
                    if best is not None and nop >= best[0][0]:
                        break
                else:
                    if best is None or (nop, nop / len(Y), p) < best[0]:
                        best = ((nop, nop / len(Y), p), (score, ns, p, L2, Y, cov), wit)
                    if nop == 0:
                        break
            _, (score, ns, p, L2, Y, cov), wit = best
        rq = p
        while L2 % (rq * p) == 0:
            rq *= p
        if STATS:
            STATS.write(f"{L2.bit_length()} {p} {len(Y)} {sum(1 for c, w in zip(cov, wit) if not c and not w)}\n")
        rec['split'] = p; rec['children'] = []
        nsurv = 0
        for y, c, w in zip(Y, cov, wit):
            ch = {'x': y, 'L': L2}
            rec['children'].append(ch)
            if c:
                M, res, (fam, P) = D.witness(y, L2, Mmax)
                ch['leaf'] = [M, res, fam, list(P)]
            elif w:
                fam, P = w
                M, r = modres(fam, P, y)
                ch['leaf'] = [M, r, fam, list(P)]; cw += 1
            elif w is False:   # known open w.r.t. M | L2: push with a mark (no re-query needed)
                heapq.heappush(heap, (-mass / len(Y), cnt, L2, y, -1, ch)); cnt += 1; nsurv += 1
            else:
                heapq.heappush(heap, (-mass / len(Y), cnt, L2, y, rq, ch)); cnt += 1; nsurv += 1
        if nodes % 200 == 0:
            om = sum(-s[0] for s in heap)
            print(f"nodes={nodes} queue={len(heap)} openmass={om:.3e} Cwit={cw} split={p} "
                  f"surv={nsurv}/{len(Y)} Cq={nC[0]} t={time.time()-t0:.0f}s", flush=True)
    print(f"done nodes={nodes} open={len(open_leaves)} openmass={openmass:.4e} Cwit={cw} t={time.time()-t0:.0f}s")
    for L, x, m in sorted(open_leaves, key=lambda z: -z[2])[:10]:
        print("open", x, L, f"{m:.2e}")
    json.dump(tree, (gzip.open if out.endswith('.gz') else open)(out, 'wt'))


if __name__ == '__main__':
    main()
