#!/usr/bin/env python3
"""Z1201: decision-diagram size for divisor selection with a target residue.

Divisors of N = prod q_i^{a_i} are paths through levels i = 0..k-1 (choose exponent j_i in
[0,a_i]); the path is accepted iff prod q_i^{j_i} = t (mod m). A reduced ordered decision
diagram (ZDD/MDD-style) merges nodes with the same subfunction. At level i, a prefix with
partial residue s accepts exactly the tails c (c = product over levels >= i, residue mod m)
with s*c = t (mod m), so the subfunction is determined by the set
   Acc_i(s) = { c in C_i : s*c = t (mod m) },   C_i = attainable tail residues.
Node count at level i = number of distinct nonempty Acc_i(s) over reachable prefix residues s
(zero-suppression: the empty set is the 0-terminal). Compared with tau(N) = number of paths.
Checked: the number of accepted leaves equals the direct divisor count.
"""
import sys, json, random, time
from fractions import Fraction

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def build(pps, m, t):
    k = len(pps)
    # tail residue sets C_i (backward), as sets of residues mod m
    C = [None] * (k + 1)
    C[k] = {1 % m}
    for i in range(k - 1, -1, -1):
        q, a = pps[i]
        C[i] = {(pow(q, j, m) * c) % m for j in range(a + 1) for c in C[i + 1]}
    # forward prefix residues S_i
    S = [set() for _ in range(k + 1)]
    S[0] = {1 % m}
    for i in range(k):
        q, a = pps[i]
        S[i + 1] = {(s * pow(q, j, m)) % m for s in S[i] for j in range(a + 1)}
    nodes_levels = []
    distinct_prefix = []
    for i in range(k):
        keys = set()
        for s in S[i]:
            acc = frozenset(c for c in C[i] if (s * c - t) % m == 0)
            if acc:
                keys.add(acc)
        nodes_levels.append(len(keys))
        distinct_prefix.append(len(S[i]))
    # accepted leaves via multiplicity DP (independent of the node construction)
    mult = {1 % m: 1}
    for i in range(k):
        q, a = pps[i]
        new = {}
        for s_, c_ in mult.items():
            for j in range(a + 1):
                key = (s_ * pow(q, j, m)) % m
                new[key] = new.get(key, 0) + c_
        mult = new
    accepted = mult.get(t % m, 0)
    tau = 1
    for q, a in pps:
        tau *= (a + 1)
    return sum(nodes_levels), nodes_levels, distinct_prefix, tau, accepted

def direct(pps, m, t):
    ds = [1]
    for q, a in pps:
        ds = [d * q ** j for d in ds for j in range(a + 1)]
    return sum(1 for d in ds if (d - t) % m == 0), len(ds)

def random_check(trials=400, seed=3):
    rnd = random.Random(seed)
    bad = 0
    for _ in range(trials):
        N = rnd.randint(4, 10 ** 5); m = rnd.randint(2, 300); t = rnd.randint(0, m - 1)
        pps = sorted(factor(N).items())
        nodes, lv, dp, tau, acc = build(pps, m, t)
        cnt, _ = direct(pps, m, t)
        if cnt != acc:
            bad += 1
    return trials, bad

def es_rows(pmax=1000, K=6):
    ps = [p for p in range(5, pmax) if p % 4 == 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))]
    rows = []
    for p in ps:
        x0 = -(-p // 4)
        for x in range(x0, x0 + K):
            r = 4 * x - p; M = p * x
            pps = sorted(factor(M * M).items())
            t = (-M) % r
            nodes, lv, dp, tau, _ = build(pps, r, t)
            cnt, _ = direct(pps, r, t)
            _, _, _, _, acc = build(pps, r, t)
            assert acc == cnt
            rows.append({"p": p, "x": x, "r": r, "tau": tau, "dd_nodes": nodes, "levels": lv,
                         "prefix_residues_max": max(dp), "solutions": cnt})
    return rows

if __name__ == "__main__":
    t0 = time.time()
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    tr, bad = random_check()
    print(f"random check (DD accepted leaves == direct count): trials={tr} mismatches={bad}")
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rows = es_rows(pmax, K)
    # accepted-count consistency: the DD must accept exactly the direct solutions
    tot_tau = sum(r["tau"] for r in rows)
    tot_nodes = sum(r["dd_nodes"] for r in rows)
    print(f"ES windows: {len(rows)} (p<={pmax}, {K} windows each; max r={max(r['r'] for r in rows)})")
    print(f"sum tau(M^2)={tot_tau}  sum DD nodes={tot_nodes}  ratio={tot_nodes/tot_tau:.4f}")
    big = max(rows, key=lambda r: r["tau"])
    print("largest tau row:", {k: big[k] for k in ("p", "x", "r", "tau", "dd_nodes", "solutions")})
    ratios = sorted(r["dd_nodes"] / r["tau"] for r in rows)
    print("DD/tau ratio quantiles (min,median,max):", round(ratios[0], 4), round(ratios[len(ratios)//2], 4), round(ratios[-1], 4))
    print("windows with DD nodes > tau:", sum(1 for r in rows if r["dd_nodes"] > r["tau"]))
    print("seconds", round(time.time() - t0, 2))
    json.dump(rows, open(f"data/z52b/pass2/NC0/sub/Z1201_dd_{pmax}_{K}.json", "w"))
