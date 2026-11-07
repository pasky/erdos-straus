#!/usr/bin/env python3
"""z61 TRANSPORTO: rule R1 (unit-shift Kummer transport) for U7, as pre-registered in Z61_TRANSPORTO.md §0.

Usage:  z61_transporto_r1.py [--walk] [--hitset u7|u8] n1 n2 ...
  --walk     also run the literal token walk (cyclic fibre walk, greedy) and check it against the closed form
  --hitset   u7 (default): HIT = a_f = 1 (r_f | f+1).  u8: HIT only at U^(8) targets (r | (f+1)/8 or r = 8a, a | (f+1)/8)
Output: one JSON line per n.

Closed form (proved in the memo, §2 Lemma 1): for each (l, j), stranded(l, j) = 0 if the fibre
S_{l,j} = {f : r_f = 1 mod l^j} contains a HIT or EXIT column, else max(0, T_{l,j} - C_{l,j}), where
T = #ORDINARY columns with l^j | a_f, C = #ORDINARY columns in S_{l,j} with l^j | a_f - 1.
"""
import sys, json, math
import numpy as np

def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == 0:
            spf[i] = i
            blk = spf[i * i::i]
            m = blk == 0
            blk[m] = i
            spf[i * i::i] = blk
    z = np.nonzero(spf == 0)[0]
    spf[z] = z
    return spf

def factor(x, spf):
    out = {}
    while x > 1:
        p = int(spf[x])
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out[p] = e
    return out

def columns(n, hitset="u7"):
    """Return list of dicts for f in F(n)."""
    cols = []
    for f in range(7, 2 * n + 2, 8):
        if n % f == 0:
            continue
        k = -(-n // f)
        r = k * f - n
        d = math.gcd(r, f + 1)
        a = r // d
        if gcd_proper(n, f, k):
            typ = "E"
        elif hitset == "u7":
            typ = "H" if a == 1 else "O"
        else:
            m = (f + 1) // 8
            hit8 = (m % r == 0) or (r % 8 == 0 and m % (r // 8) == 0)
            typ = "H" if hit8 else "O"
        cols.append((f, k, r, d, a, typ))
    return cols

def gcd_proper(n, f, k):
    return math.gcd(n, f) > 1 or math.gcd(n, k) > 1

def ledger(n, spf, hitset="u7", walk=False):
    cols = columns(n, hitset)
    T = {}      # (l,j) -> number of ORDINARY tokens
    C = {}      # (l,j) -> number of capacity units in fibre
    Tex = 0     # tokens exiting at their own EXIT column
    sink = set()  # (l,j) whose fibre contains HIT/EXIT
    sinkcols = []
    tokens = []   # (l, j, f) for walk
    capunits = {}  # (l,j) -> set of f
    nH = nE = 0
    Dl = {}; Nl = {}   # unrestricted per-prime ledger over ORDINARY columns (Lemma 2 diagnostic)
    for (f, k, r, d, a, typ) in cols:
        if typ == "O":
            if a > 1:
                for l, e in factor(a, spf).items():
                    Dl[l] = Dl.get(l, 0) + e
            if a > 2:
                for l, e in factor(a - 1, spf).items():
                    Nl[l] = Nl.get(l, 0) + e
        if typ == "O" or typ == "E":
            if a > 1 and typ == "O":
                for l, e in factor(a, spf).items():
                    for j in range(1, e + 1):
                        T[(l, j)] = T.get((l, j), 0) + 1
                        if walk:
                            tokens.append((l, j, f))
            elif a > 1 and typ == "E":
                Tex += sum(factor(a, spf).values())
        if typ == "O" and a > 2:
            for l, e in factor(a - 1, spf).items():
                for j in range(1, e + 1):
                    if (r - 1) % (l ** j) == 0:
                        C[(l, j)] = C.get((l, j), 0) + 1
                        if walk:
                            capunits.setdefault((l, j), set()).add(f)
        if typ in "HE":
            if typ == "H":
                nH += 1
            else:
                nE += 1
            sinkcols.append((f, r, typ))
    # fibres containing a sink: (l,j) with l^j | r_f - 1 for a sink column (r=1 sinks hit every fibre)
    r1sink = any(r == 1 for (_, r, _) in sinkcols)
    def fibre_has_sink(l, j):
        if r1sink:
            return True
        q = l ** j
        return any((r - 1) % q == 0 for (_, r, _) in sinkcols)
    stranded = {}
    hitused = {}
    for key, t in T.items():
        c = C.get(key, 0)
        if t > c:
            if fibre_has_sink(*key):
                hitused[key] = t - c
            else:
                stranded[key] = t - c
    res = dict(n=n, hitset=hitset, ncols=len(cols), nH=nH, nE=nE,
               tokens=sum(T.values()) + Tex, tok_exit_own=Tex,
               capacity=sum(C.values()),
               surplus_fibres=len(hitused) + len(stranded),
               sink_routed=sum(hitused.values()),
               stranded=sum(stranded.values()),
               stranded_fibres=sorted(([l, j, s] for (l, j), s in stranded.items()), key=lambda x: -x[0])[:12],
               forced=sum(max(0, v - Nl.get(l, 0)) for l, v in Dl.items()),
               forced_primes=sum(1 for l, v in Dl.items() if v > Nl.get(l, 0)),
               valid=(sum(stranded.values()) == 0))
    if walk:
        res["walk_stranded"] = run_walk(cols, tokens, capunits)
        res["walk_agrees"] = (res["walk_stranded"] == res["stranded"])
    return res

def run_walk(cols, tokens, capunits):
    """Literal R1 walk: tokens in increasing (l,j,f); cyclic walk on S_{l,j} from first column after f."""
    typ_of = {f: typ for (f, k, r, d, a, typ) in cols}
    r_of = {f: r for (f, k, r, d, a, typ) in cols}
    fs = [c[0] for c in cols]
    tokens.sort()
    stranded = 0
    fibre_cache = {}
    used = set()
    for (l, j, f) in tokens:
        q = l ** j
        if (l, j) not in fibre_cache:
            fibre_cache[(l, j)] = [g for g in fs if (r_of[g] - 1) % q == 0]
        S = fibre_cache[(l, j)]
        # start index: first column after f (cyclic)
        import bisect
        i0 = bisect.bisect_right(S, f)
        cap = capunits.get((l, j), set())
        done = False
        for step in range(len(S)):  # potential: unvisited columns of S
            g = S[(i0 + step) % len(S)]
            t = typ_of[g]
            if t in "HE":
                done = True
                break
            if g in cap and (g, l, j) not in used:
                used.add((g, l, j))
                done = True
                break
        if not done:
            stranded += 1
    return stranded

def main():
    args = sys.argv[1:]
    walk = False
    hitset = "u7"
    ns = []
    i = 0
    while i < len(args):
        if args[i] == "--walk":
            walk = True
        elif args[i] == "--hitset":
            hitset = args[i + 1]
            i += 1
        else:
            ns.append(int(args[i]))
        i += 1
    spf = spf_sieve(2 * max(ns) + 2)
    for n in ns:
        print(json.dumps(ledger(n, spf, hitset, walk)), flush=True)

if __name__ == "__main__":
    main()
