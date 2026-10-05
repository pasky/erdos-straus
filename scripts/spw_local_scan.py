"""O40: scan local (single-modulus) SPW bounds over smooth moduli e in (CN, Emax] (EVIDENCE: LP floats).
usage: spw_local_scan.py C Emax N [N ...]   -- e ranges over 7-smooth and 11-smooth numbers in (CN, Emax]"""
import sys
sys.path.insert(0, "scripts")
from spw_local_lp import local_sigma

def smooth(B, P):
    out = {1}
    for p in P:
        new = set()
        for x in out:
            y = x
            while y <= B:
                new.add(y); y *= p
        out = new
    return sorted(out)

C = float(sys.argv[1]); Emax = int(sys.argv[2])
for N in map(int, sys.argv[3:]):
    es = [e for e in smooth(Emax, [2, 3, 5, 7, 11]) if e > C * N]
    best = []
    for e in es:
        s, ns = local_sigma(N, C, e)
        best.append((s, e, ns))
    best.sort()
    print(f"N={N}: #e={len(es)}; worst:", ", ".join(f"e={e}:{s:.4f}" for s, e, ns in best[:6]), flush=True)
