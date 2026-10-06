"""Adaptive branching covering search for Sigma_r by ES polynomial classes (task O80).

usage: mordell_dfs.py r variant Mmax Pmax emax maxnodes [out.json] [root_filter]
  For every uncovered node (x mod L) choose the refinement q (a new prime <= Pmax, or one
  more power of a prime already in L, exponent <= emax) with the fewest uncovered children;
  recurse.  Classes: all seven ET families, modulus M | L, M <= Mmax.
  Output: tree certificate (json) with, for each leaf, a witness class.
  root_filter (optional) 'a:m' keeps only root nodes x = a (mod m).
"""
import sys, json, time, heapq
import numpy as np
from math import gcd
import os
import mordell_lib
from mordell_lib import divisors, residue_table, residue_set
mordell_lib.I1_CAP[0] = int(float(os.environ.get('MORDELL_I1CAP', '0')))
from mordell_cover import base, primes_upto

TABLE = {}
def table(M):
    t = TABLE.get(M)
    if t is None:
        w = residue_set(M)
        t = (np.array(sorted(w), dtype=np.int64), None)
        TABLE[M] = t
    return t

DIVC = {}
BOUND = [10 ** 8]
def divs(L):
    """divisors of L that are <= BOUND[0] (L is smooth)"""
    d = DIVC.get(L)
    if d is None:
        B = BOUND[0]
        d = [1]
        n = L
        p = 2
        while n > 1:
            if n % p == 0:
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                d = [a * p ** i for a in d for i in range(e + 1) if a * p ** i <= B]
            p += 1
        d.sort()
        DIVC[L] = d
    return d

def covered_by(x, L, T, moduli):
    """mask: child x + L*t (t in T) covered by a class with modulus in moduli"""
    cov = np.zeros(len(T), dtype=bool)
    for M in moduli:
        a, w = table(M)
        if len(a) == 0:
            continue
        idx = np.nonzero(~cov)[0]
        if len(idx) == 0:
            break
        y = (x % M + (L % M) * T[idx]) % M
        i = np.searchsorted(a, y)
        i[i == len(a)] = 0
        hit = a[i] == y
        cov[idx[hit]] = True
    return cov

def witness(x, L, Mmax):
    for M in divs(L):
        if M > Mmax or M < 3:
            continue
        a, _ = table(M)
        r = x % M
        i = np.searchsorted(a, r)
        if i < len(a) and a[i] == r:
            w = residue_table(M)
            return (M, r, w[r])
    return None

def new_moduli(L, q, p, Mmax):
    """moduli dividing L' = L*(q or p) but not L, <= Mmax"""
    if L % p == 0:
        e = 0
        while L % p ** (e + 1) == 0:
            e += 1
        pe1 = p ** (e + 1)
        Lc = L // p ** e
        return sorted(d * pe1 for d in divs(Lc) if d * pe1 <= Mmax), L * p
    return sorted(d * q for d in divs(L) if d * q <= Mmax), L * q

def main():
    r = int(sys.argv[1]); variant = sys.argv[2]; Mmax = int(sys.argv[3])
    Pmax = int(sys.argv[4]); emax = int(sys.argv[5]); maxnodes = int(sys.argv[6])
    out = sys.argv[7] if len(sys.argv) > 7 else None
    rootf = sys.argv[8] if len(sys.argv) > 8 else None
    BOUND[0] = Mmax
    L0, X0 = base(r, variant)
    if rootf:
        a, m = map(int, rootf.split(':'))
        X0 = X0[X0 % m == a]
    PR = primes_upto(Pmax)
    t0 = time.time()
    tree = {'r': r, 'variant': variant, 'L0': L0, 'Mmax': Mmax, 'roots': []}
    nodes = 0
    open_leaves = []
    # each stack item: (L, x, record-dict)
    stack = []   # heap keyed by -measure (largest open mass first)
    cnt = 0
    m0 = 1.0 / len(X0)
    for x in X0.tolist():
        rec = {'x': x, 'L': L0}
        tree['roots'].append(rec)
        heapq.heappush(stack, (-m0, cnt, L0, x, rec)); cnt += 1
    openmass = 0.0
    while stack:
        negm, _, L, x, rec = heapq.heappop(stack)
        mass = -negm
        nodes += 1
        if nodes > maxnodes:
            rec['open'] = True
            open_leaves.append((L, x))
            openmass += mass
            continue
        wv = witness(x, L, Mmax)
        if wv is not None:
            M, res, (fam, P) = wv
            rec['leaf'] = [M, res, fam, list(P)]
            continue
        best = None
        cands = []
        for p in PR:
            if L % p == 0:
                e = 0
                while L % p ** (e + 1) == 0:
                    e += 1
                if e < (emax + 3 if p == 2 else emax + 1 if p == 3 else emax):
                    cands.append((p ** (e + 1), p))
            else:
                cands.append((p, p))
        for q, p in cands:
            mods, L2 = new_moduli(L, q, p, Mmax)
            t = np.arange(p, dtype=np.int64)
            T = t[(x % p + (L % p) * t) % p != 0]
            cov = covered_by(x, L, T, mods)
            Y = [x + L * int(tt) for tt in T]
            ns = int((~cov).sum())
            score = ns / (p - 1)
            if best is None or score < best[0]:
                best = (score, q, p, L2, Y, cov)
            if ns == 0:
                break
        if best is None:
            rec['open'] = True
            open_leaves.append((L, x))
            openmass += mass
            continue
        score, q, p, L2, Y, cov = best
        rec['split'] = p
        rec['children'] = []
        for y, c in zip(Y, cov.tolist()):
            ch = {'x': y, 'L': L2}
            rec['children'].append(ch)
            if not c:
                heapq.heappush(stack, (-mass / len(Y), cnt, L2, y, ch)); cnt += 1
            else:
                M, res, (fam, P) = witness(y, L2, Mmax)
                ch['leaf'] = [M, res, fam, list(P)]
        if nodes % 200 == 0:
            om = sum(-s[0] for s in stack)
            print(f"nodes={nodes} queue={len(stack)} openmass={om:.3e} curmass={mass:.2e} split={q} surv={int((~cov).sum())}/{p-1} t={time.time()-t0:.0f}s", flush=True)
    print(f"done nodes={nodes} open={len(open_leaves)} openmass={openmass:.4e} t={time.time()-t0:.0f}s")
    if open_leaves:
        from collections import Counter
        print("open sample:", open_leaves[:5])
    if out:
        json.dump(tree, open(out, 'w'))

if __name__ == '__main__':
    main()
