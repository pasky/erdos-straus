"""z52b pass-1 batch U08: exact enumeration of 3-term unit-fraction representations a/p = 1/x+1/y+1/z.

Used by the U08 items Z0716 (nx(p) = number of distinct smallest denominators), Z0290 (prime-type denominator world)
and Z0203 (representability of a/p for small numerators a).

Method: fix the smallest denominator x in (p/a, 3p/a]. With A = a x - p, B = p x, one has 1/y+1/z = A/B, equivalent to
(Ay-B)(Az-B) = B^2. So u = Ay-B runs over divisors of B^2 with u ≡ -B (mod A) and v = B^2/u. Requires y >= x.
Full divisor enumeration of B^2 from factorisation (sympy). Memory is O(#divisors of B^2) per x.

Usage: uv run --with sympy python scripts/z52b_p1_U08_enum.py <mode> ...
"""
import sys, math, json, os, time
from sympy import primerange, factorint, isprime


def divisors_from_factor(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def reps(a, p, need_all=True):
    """All triples x<=y<=z of positive integers with a/p = 1/x+1/y+1/z (returns list of tuples)."""
    out = []
    fp = factorint(p)
    xlo = p // a + 1           # x > p/a
    xhi = 3 * p // a           # x <= 3p/a
    for x in range(max(xlo, 1), xhi + 1):
        A = a * x - p
        if A <= 0:
            continue
        B = p * x
        fac = {q: 2 * e for q, e in fp.items()}
        for q, e in factorint(x).items():
            fac[q] = fac.get(q, 0) + 2 * e
        for u in divisors_from_factor(fac):
            if (u + B) % A:
                continue
            v = (B * B) // u
            if (v + B) % A:
                continue
            y = (u + B) // A
            z = (v + B) // A
            if y < x or z < y:
                continue
            out.append((x, y, z))
            if not need_all:
                return out
    return out


def nx_of(sols):
    return len({s[0] for s in sols})


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "test":
        for p in [5, 13, 17, 37, 1009]:
            t = time.time()
            r = reps(4, p)
            print(p, len(r), nx_of(r), round(time.time() - t, 2))


def _load_U():
    import numpy as np
    F = np.loadtxt("data/z52b/raw/f4_all_30000.txt", dtype=np.int64)
    return dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))


def _mode_nx_world(lo, hi, outdir):
    """Z0716 (nx(p) vs log p) and Z0290 (prime-type denominator world) on primes p ≡ 1 (mod 4), lo < p <= hi."""
    Ud = _load_U()
    ps = [p for p in primerange(lo, hi + 1) if p % 4 == 1]
    primes_set = set(primerange(2, 3 * hi + 10))
    rows, world_pt, world_x, mism = [], 0, 0, []
    for p in ps:
        sols = reps(4, p)
        U = len(sols)
        if Ud.get(p) is not None and Ud[p] != U:
            mism.append((p, U, Ud[p]))
        nx = nx_of(sols)
        # Z0290: all denominators in {p} ∪ primes ∪ 2·primes  (and x-only prime test)
        def ok(d):
            return d == p or d in primes_set or (d % 2 == 0 and (d // 2) in primes_set)
        pt = any(ok(x) and ok(y) and ok(z) for x, y, z in sols)
        px = any(x in primes_set and x != p and (x in primes_set) for x, y, z in sols)  # smallest denom prime
        pxall = any(all(d in primes_set for d in s) for s in sols)
        world_pt += pt
        world_x += pxall
        rows.append(dict(p=p, U=U, nx=nx, pt=bool(pt), allprime=bool(pxall)))
    import math
    n = len(rows)
    lp = [math.log(r["p"]) for r in rows]
    nxs = [r["nx"] for r in rows]
    Us = [r["U"] for r in rows]
    def corr(a, b):
        ma, mb = sum(a) / len(a), sum(b) / len(b)
        sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((y - mb) ** 2 for y in b))
        return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)
    summ = dict(n_primes=n, lo=lo, hi=hi, U_mismatch_vs_f4=mism[:10], n_mismatch=len(mism),
                corr_nx_logp=corr(nxs, lp), corr_nx_logsq=corr(nxs, [l * l for l in lp]),
                mean_nx_by_decade={}, world_prime_denoms_pt=world_pt, world_all_prime_denoms=world_x,
                no_solution_pt=[r["p"] for r in rows if not r["pt"]][:40])
    # mean nx in ranges of p
    for lo2 in [5, 100, 500, 1000, 2000, 4000]:
        sel = [r["nx"] for r in rows if lo2 <= r["p"] < lo2 * 2 if lo2 * 2 <= hi + 1] or None
        if sel:
            summ["mean_nx_by_decade"][f"[{lo2},{2*lo2})"] = round(sum(sel) / len(sel), 3)
    os.makedirs(outdir, exist_ok=True)
    json.dump(dict(summary=summ, rows=rows), open(os.path.join(outdir, "nx_world.json"), "w"))
    print(json.dumps({k: v for k, v in summ.items() if k != "no_solution_pt"}, indent=1))
    print("no pt-world solution (first 40):", summ["no_solution_pt"])


def _mode_rep(pmax, avals, outdir):
    """Z0203: fraction of primes p <= pmax for which a/p has a 3-term unit-fraction representation."""
    res = {}
    ps = list(primerange(3, pmax + 1))
    for a in avals:
        cnt = 0
        fails = []
        for p in ps:
            if reps(a, p, need_all=False):
                cnt += 1
            else:
                fails.append(p)
        res[a] = dict(n=len(ps), representable=cnt, frac=round(cnt / len(ps), 5), first_fails=fails[:12])
        print(a, res[a], flush=True)
    os.makedirs(outdir, exist_ok=True)
    json.dump(res, open(os.path.join(outdir, "rep_a.json"), "w"), indent=1)


if __name__ == "__main__" and len(sys.argv) > 1:
    if sys.argv[1] == "nxworld":
        _mode_nx_world(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif sys.argv[1] == "rep":
        _mode_rep(int(sys.argv[2]), [int(v) for v in sys.argv[3].split(",")], sys.argv[4])
