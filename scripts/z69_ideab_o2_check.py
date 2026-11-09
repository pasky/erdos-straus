#!/usr/bin/env python3
"""Kill test B for z69_ideab_o2.py: recompute lambda(p) by DIRECT divisibility tests on the defining conditions of the
seven families (no residue table, no CRT, no modular inverses) and compare with the table-based value.
usage: o2_check.py JSON MMAX NRANDOM"""
import sys, json, math, random, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("o2", "scripts/z69_ideab_o2.py"); o2 = importlib.util.module_from_spec(spec)
sys.argv_backup = sys.argv; sys.argv = ["o2", "1e6", "8", "2"]; spec.loader.exec_module(o2); sys.argv = sys.argv_backup
J = json.load(open(sys.argv[1])); MMAX = int(sys.argv[2]); NR = int(sys.argv[3])

def direct_lambda(p, limit):
    best = limit + 1
    Q = limit // 4
    for a in range(1, Q + 1):
        for b in range(a, Q // a + 1):
            M = 4 * a * b
            if M >= best: break
            s = a + b
            for e in range(1, s + 1):
                if s % e == 0 and ((p + e) % M == 0 or (p * e + 1) % M == 0): best = min(best, M)      # II-1, I-4
    for f in range(3, min(limit, best - 1) + 1, 4):                                                      # II-2
        k = (f + 1) // 4
        for a in range(1, k + 1):
            if k % a: continue
            for d in range(1, k // a + 1):
                if (k // a) % d == 0 and (p + 4 * a * a * d) % f == 0: best = min(best, f)
    for a in range(1, Q + 1):                                                                            # I-1
        for d in range(1, Q // a + 1):
            M = 4 * a * d
            if M >= best: break
            N = 4 * a * a * d + 1
            f = (-p) % M
            while f <= N:
                if f > 0 and N % f == 0: best = min(best, M); break
                f += M
    for f in range(3, Q + 1, 4):                                                                         # I-2, I-3, II-3
        for u in range(1, Q // f + 1):
            for v in range(1, Q // (f * u) + 1):
                M = 4 * u * v * f
                if M >= best: break
                if math.gcd(4 * u * v, f) != 1 or (p + f) % (4 * u * v): continue
                if (u * p + v) % f == 0 or (p * p + 4 * u * u * v) % f == 0 or (p + 4 * u * u * v) % f == 0:
                    best = min(best, M)
    return best

cls = o2.build(MMAX); mods = sorted(cls)
def table_lambda(p):
    for M in mods:
        if p % M in cls[M]: return M
    return MMAX + 1
random.seed(69); bad = 0; n = 0
for r, D in J.items():
    recs = [q for q, _ in D["records"]]
    n0 = next(1 + 840 * t for t in range(11) if (1 + 840 * t) % 11 == int(r))
    P = o2.primes_in_class(n0, 9240, 3 * 10**8).tolist()
    sample = recs + random.sample(P, NR)
    for p in sample:
        lt = table_lambda(p); ld = direct_lambda(p, MMAX); n += 1
        if lt != ld: bad += 1; print("MISMATCH", r, p, lt, ld)
    print(f"r={r}: checked {len(sample)} primes (all {len(recs)} record setters + {NR} random < 3e8)", flush=True)
print("total checked:", n, " mismatches:", bad)
