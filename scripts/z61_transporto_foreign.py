#!/usr/bin/env python3
"""z61 TRANSPORTO: 'foreign flux' screen at primes (fable's 169 exit-capacity screen transposed to hits).

For n, over ORDINARY columns compute the forced primes  Fp = {l : sum v_l(a_f) > sum v_l(a_f - 1)}  (Lemma 2: nonempty
whenever an ORDINARY column exists). For the sink columns (HIT at primes, EXIT at composites) compute the generous
local carrier set  Hc = primes dividing  f (f+1) k (n+k) r (r-1) a  for some sink column (r = r_f, k = k_f).
Carriers are the NONZERO quantities among these (convention NZ: nUncovered); convention Z additionally lets a zero
quantity (r - 1 = 0 at an r = 1 sink) carry every l (nUncovered_Z). Report |Fp|, |Fp minus Hc|. A rule in which a sink may absorb an l-token only if l divides one of these local quantities
of the sink ("valuation-faithful sink") cannot be valid at n when Fp minus Hc is nonempty.
Usage: z61_transporto_foreign.py PMAX  -> data/z61/transporto/foreign.jsonl
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(__file__))
from z61_transporto_r1 import spf_sieve, factor, columns

ROOT = os.path.join(os.path.dirname(__file__), "..")

def foreign(n, spf):
    cols = columns(n, "u7")
    D, N = {}, {}
    sinkprimes = set()
    for (f, k, r, d, a, typ) in cols:
        if typ == "O":
            for l, e in factor(a, spf).items():
                D[l] = D.get(l, 0) + e
            if a > 2:
                for l, e in factor(a - 1, spf).items():
                    N[l] = N.get(l, 0) + e
        else:
            for q in (f, f + 1, k, n + k, r, r - 1, a):
                if q > 1:
                    sinkprimes.update(factor(q, spf).keys()) if q < len(spf) else sinkprimes.update(
                        factor_big(q, spf).keys())
    Fp = {l for l, v in D.items() if v > N.get(l, 0)}
    unc = sorted(Fp - sinkprimes)
    # convention Z: a zero carrier (r - 1 = 0 at an r = 1 sink) is divisible by every l, so such a sink is universal
    zero_universal = any(c[5] != "O" and c[2] == 1 for c in cols)
    return dict(n=n, nsink=sum(1 for c in cols if c[5] != "O"), nF=len(Fp), nUncovered=len(unc),
                nUncovered_Z=0 if zero_universal else len(unc), uncovered_top=unc[-8:])

def factor_big(q, spf):
    out = {}
    p = 2
    while p * p <= q:
        while q % p == 0:
            out[p] = out.get(p, 0) + 1
            q //= p
        p += 1
    if q > 1:
        out[q] = out.get(q, 0) + 1
    return out

def main():
    PMAX = int(sys.argv[1])
    extra = [169, 289, 361, 529, 105, 1465, 3865, 4545, 10305, 12145, 39361, 67425,
             409, 577, 5569, 9601, 23929, 83449, 102001, 193, 673, 1489, 2521, 20641, 21841, 28921, 66529]
    spf = spf_sieve(4 * max(PMAX, max(extra)) + 4)
    ns = [p for p in range(13, PMAX + 1, 2) if spf[p] == p] + extra
    with open(os.path.join(ROOT, "data/z61/transporto/foreign.jsonl"), "w") as fo:
        for n in ns:
            fo.write(json.dumps(foreign(n, spf)) + "\n")

if __name__ == "__main__":
    main()
