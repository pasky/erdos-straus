#!/usr/bin/env python3
"""z62 PARITY — non-local (graph-degree) weights, Lemma P0(b)-type: w(c) = number of OTHER words sharing a datum with c.
Relations: same u, same v, same t, same sigma=u+v, same A=tu-1 (as a divisor), same min(u,v), same max(u,v).
Neighbour pools: all words of X(n) (ALLX) or the family itself. Counts W(n) = sum over family words of deg mod 2.
Writes a TSV usable by z62_parity_gf2.py.  Usage: z62_parity_nonlocal.py NMAX [extra n ...]
"""
import sys
from math import isqrt
from collections import Counter
sys.path.insert(0, "scripts")
import z62_parity_river as Z

KEYS = {"u": lambda w: ("u", w[1]), "v": lambda w: ("v", w[2]), "t": lambda w: ("t", w[0]),
        "s": lambda w: ("s", w[1] + w[2]), "A": lambda w: ("A", w[0] * w[1] - 1),
        "uv": lambda w: ("uv", w[1] * w[2]), "tu": lambda w: ("tu", w[0] * w[1])}
FAMS = ("STAR", "U7", "ALLX")


def row(n):
    ws = [w for w in Z.words(n)]
    fl = {w: Z.fam_flags(n, *w) for w in ws}
    out = {}
    for f in FAMS:
        fam = [w for w in ws if fl[w][f]]
        out[f"{f}_one"] = len(fam)
        for pool_name, pool in (("all", ws), ("fam", fam)):
            for k, key in KEYS.items():
                cnt = Counter(key(w) for w in pool)
                tot = 0
                for w in fam:
                    d = cnt[key(w)] - (1 if (pool is fam or fl[w][f]) and w in set(pool) else 0)
                    tot += d
                out[f"{f}_deg{k}_{pool_name}"] = tot
    return out


def main():
    N = int(sys.argv[1]); extra = [int(x) for x in sys.argv[2:]]
    Z.SPF = Z.spf_sieve(N + isqrt(N) + 10)
    ns = [p for p in range(25, N + 1, 24) if Z.is_prime(p)] + extra
    hdr = None
    for n in ns:
        r = row(n)
        if hdr is None:
            hdr = list(r)
            print("n\ttag\t" + "\t".join(hdr))
        rt = isqrt(n)
        tag = "SQ" if rt * rt == n else ("P" if Z.is_prime(n) else "C")
        print(f"{n}\t{tag}\t" + "\t".join(str(r[h]) for h in hdr), flush=True)


if __name__ == "__main__":
    main()
