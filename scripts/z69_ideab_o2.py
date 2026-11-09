#!/usr/bin/env python3
"""z69 IDEAB Phase 3: integer-side test of open problem O2 of Z66_UCOVER.md.
lambda(p) := least modulus of an ET Prop 1.9 family class (I-1, I-2, I-3, I-4, II-1, II-2, II-3) containing the prime p.
Classes are enumerated as SUPERSETS of ET's (no coprimality side conditions beyond those needed for unit residues), so
"lambda(p) > M" computed here implies the same for ET's families.
  II-1: -e      mod 4ab, e | a+b          I-4: -1/e mod 4ab, e | a+b
  II-2: -4a^2 d mod f,   4ad | f+1        I-1: -f   mod 4ad, f | 4a^2 d + 1
  I-2 : -f mod 4ac  &  -c/a mod f         I-3: -f   mod 4cd  &  n^2 = -4c^2 d mod f     II-3: -e mod 4ad & -4a^2 d mod e
usage: o2.py XMAX MMAX r [r ...]      (classes n = 1 mod 840, n = r mod 11; r = 1 is the square-class control)
"""
import sys, math, json
import numpy as np
from collections import defaultdict
from sympy import divisors

XMAX = int(float(sys.argv[1])); MMAX = int(sys.argv[2]); RS = [int(x) for x in sys.argv[3:]]

def build(MMAX):
    cls = defaultdict(set)
    Q = MMAX // 4
    for a in range(1, Q + 1):                                   # II-1, I-4
        for b in range(a, Q // a + 1):
            M = 4 * a * b
            for e in divisors(a + b):
                if math.gcd(e, M) == 1:
                    cls[M].add((-e) % M); cls[M].add((-pow(e, -1, M)) % M)
    for f in range(3, MMAX + 1, 4):                              # II-2
        k = (f + 1) // 4
        for a in divisors(k):
            for d in divisors(k // a): cls[f].add((-4 * a * a * d) % f)
    for a in range(1, Q + 1):                                   # I-1
        for d in range(1, Q // a + 1):
            M = 4 * a * d
            for f in divisors(4 * a * a * d + 1): cls[M].add((-f) % M)
    sq = {}                                                      # square roots mod f, f = 3 mod 4
    def roots(f):
        if f not in sq:
            t = defaultdict(list)
            for x in range(f): t[x * x % f].append(x)
            sq[f] = t
        return sq[f]
    for f in range(3, Q + 1, 4):                                 # I-2, I-3, II-3 (modulus 4*u*v*f)
        for u in range(1, Q // f + 1):
            for v in range(1, Q // (f * u) + 1):
                m4 = 4 * u * v
                if math.gcd(m4, f) != 1: continue
                M = m4 * f; inv_m4 = pow(m4, -1, f)
                def crt(r4, rf):           # x = r4 mod m4, x = rf mod f
                    return (r4 + m4 * ((rf - r4) * inv_m4 % f)) % M
                r4 = (-f) % m4
                cls[M].add(crt(r4, (-v * pow(u, -1, f)) % f))               # I-2 with (a,c) = (u,v)
                for x in roots(f).get((-4 * u * u * v) % f, []):            # I-3 with (c,d) = (u,v)
                    cls[M].add(crt(r4, x))
                cls[M].add(crt(r4, (-4 * u * u * v) % f))                   # II-3 with (a,d) = (u,v), e = f
    return cls

def primes_in_class(n0, step, XMAX):
    T = (XMAX - n0) // step + 1
    alive = np.ones(T, dtype=bool)
    lim = int(math.isqrt(XMAX)) + 1
    sieve = np.ones(lim + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(lim ** 0.5) + 1):
        if sieve[i]: sieve[i * i::i] = False
    for q in np.nonzero(sieve)[0].tolist():
        if step % q == 0: continue
        t0 = (-n0 * pow(step, -1, q)) % q
        alive[t0::q] = False
        v = n0 + step * t0
        if v == q and t0 < T: alive[t0] = True                    # q itself is prime
    idx = np.nonzero(alive)[0]
    p = n0 + step * idx.astype(np.int64)
    return p[p > 1]

if __name__ == "__main__":
    cls = build(MMAX)
    mods = sorted(cls)
    print(f"XMAX={XMAX:.3g} MMAX={MMAX}: {len(mods)} moduli, {sum(len(v) for v in cls.values())} classes", flush=True)
    out = {}
    for r in RS:
        n0 = next(1 + 840 * t for t in range(11) if (1 + 840 * t) % 11 == r)
        p = primes_in_class(n0, 9240, XMAX)
        lam = np.zeros(len(p), dtype=np.int32); idx = np.arange(len(p))
        for M in mods:
            if len(idx) == 0: break
            g = math.gcd(M, 9240)
            res = [x for x in cls[M] if x % g == n0 % g]
            if not res: continue
            hit = np.isin(p[idx] % M, np.array(res, dtype=np.int64))
            lam[idx[hit]] = M; idx = idx[~hit]
        unres = p[lam == 0]
        eff = np.where(lam == 0, MMAX + 1, lam)
        recs = []; cur = 0
        runmax = np.maximum.accumulate(eff)
        ch = np.nonzero(np.diff(np.concatenate(([0], runmax))))[0]
        recs = [(int(p[i]), int(eff[i])) for i in ch]
        dec = []
        for e10 in range(4, int(math.log10(XMAX)) + 1):
            m = p <= 10 ** e10
            if m.any(): dec.append((e10, int(m.sum()), int(eff[m].max()), float(eff[m].mean())))
        print(f"r={r}: {len(p)} primes; unresolved (lambda>{MMAX}): {len(unres)} {unres[:5].tolist()}", flush=True)
        print("   decade: (log10 X, #primes, max lambda, mean lambda):", [(a, b, c, round(d, 1)) for a, b, c, d in dec], flush=True)
        print("   records (p, lambda):", recs[-14:], flush=True)
        grid = [10, 20, 30, 50, 70, 100, 150, 200, 300, 400, 500, 700, 1000, 1500, 2000, 3000, 5000]
        tail = [(M, int((eff > M).sum())) for M in grid if M <= MMAX]
        vals, cnts = np.unique(eff, return_counts=True)
        top = sorted(zip(cnts.tolist(), vals.tolist()), reverse=True)[:12]
        print("   tail (M, #{lambda > M}):", tail, flush=True)
        print("   most frequent lambda (count, modulus):", top, flush=True)
        out[r] = {"nprimes": int(len(p)), "decades": dec, "records": recs, "unresolved": unres[:50].tolist(), "tail": tail, "top": top}
    json.dump(out, open(f"data/z69/ideab/o2_X{XMAX:.0e}_M{MMAX}_r{'-'.join(map(str, RS))}.json", "w"))
