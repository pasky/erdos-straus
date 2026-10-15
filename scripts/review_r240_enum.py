"""R240 driver for scripts/review_r240_enum.gp (PARI/GP via cypari2): exact per-pattern counts of k = 1 Case B tuples at q = 9.

usage: uv run --with cypari2 python scripts/review_r240_enum.py S [--all-routes CAP] [--compat-only] [--cmp DIR]
  Output lines: "s a z y t  n_all  n_P8  n_lawfail  route"  (orientation a <= b; n_P8 = tuples with E(0)^4 = -1).
  --all-routes CAP: run every route of cost exponent <= CAP and require identical counts (cross-check).
  --compat-only: only patterns with eps(s; z, t) = (-1)^{s/4} (the ones that can carry P8 tuples by Thm 1.2).
  --maxcost C: skip (print SKIP) patterns whose chosen route has cost exponent (+1 for factoring routes) > C.
  --cmp DIR: compare n_P8 with DIR/p_S.txt (author's file), fail on any mismatch / missing pattern.
Exit code 1 on any law failure, route disagreement or mismatch.
"""
import sys, os, time
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2 * 10**9, silent=True) if hasattr(pari, "allocatemem") else None
HERE = os.path.dirname(os.path.abspath(__file__))
pari('read("%s")' % os.path.join(HERE, "review_r240_enum.gp"))


def eps(s, z, t):
    return (-1) ** ((t + t * z + z * (1 + s) + t * s) % 2)


def costs(s, a, z, y, t):
    # (cost exponent, route); factoring routes get +1 (one factor q of overhead) in the choice only
    return {1: z + a + y, 2: t, 3: z + y, 4: a + y, 5: z + a}


def main():
    args = sys.argv[1:]
    s = int(args[0])
    cap = None
    if "--all-routes" in args:
        cap = float(args[args.index("--all-routes") + 1])
    compat = "--compat-only" in args
    cmpdir = args[args.index("--cmp") + 1] if "--cmp" in args else None
    maxcost = float(args[args.index("--maxcost") + 1]) if "--maxcost" in args else None
    bad = 0
    res = {}
    t0 = time.time()
    for a in range(s + 1):
        for z in range(s + 1 - a):
            b = s - a - z
            if b < a:
                continue
            for y in range(b + 1):
                t = b - y
                if compat and (s % 4 or eps(s, z, t) != (-1) ** (s // 4)):
                    continue
                c = costs(s, a, z, y, t)
                best = min(c, key=lambda r: (c[r] + (0 if r == 1 else 1), r))
                if maxcost is not None and c[best] + (0 if best == 1 else 1) > maxcost:
                    print(s, a, z, y, t, "SKIP", flush=True)
                    continue
                routes = [best]
                if cap is not None:
                    routes = sorted(set([best] + [r for r in c if c[r] <= cap]))
                outs = {}
                for r in routes:
                    v = pari("pattern(%d,%d,%d,%d,%d,%d)" % (s, a, z, y, t, r))
                    outs[r] = tuple(int(x) for x in v)
                vals = set(o[:2] for o in outs.values())
                if len(vals) != 1:
                    print("ROUTE DISAGREEMENT", s, a, z, y, t, outs, flush=True)
                    bad += 1
                n_all, n_p8, lawf, dup = outs[best]
                if lawf:
                    bad += 1
                res[(a, z, y)] = (t, n_all, n_p8)
                print(s, a, z, y, t, n_all, n_p8, lawf, best, ("routes=" + ",".join(map(str, routes))) if cap is not None else "",
                      flush=True)
    # summaries
    tot_all = sum(v[1] for v in res.values())
    tot_p8 = sum(v[2] for v in res.values())
    p8_incompat = sum(v[2] for (a, z, y), v in res.items() if s % 4 or eps(s, z, v[0]) != (-1) ** (s // 4))
    mass = sum((2 if a < s - a - z else 1) * v[2] for (a, z, y), v in res.items()) / 9 ** (s // 2)
    print(f"# s={s}: patterns={len(res)} tuples(a<=b)={tot_all} P8(a<=b)={tot_p8} P8 in eps-incompatible patterns={p8_incompat} "
          f"P8 mass (mult 2 for a<b, weight 9^-{s//2}) = {mass:.9e}  time={time.time()-t0:.0f}s", flush=True)
    if p8_incompat:
        bad += 1
    if cmpdir:
        fn = os.path.join(cmpdir, f"p_{s}.txt")
        seen = set()
        for line in open(fn):
            f = line.split()
            ss, a, z, y, t = map(int, f[:5])
            seen.add((a, z, y))
            if f[5] == "SKIP":
                print("# author SKIP", line.strip(), "ours P8 =", res.get((a, z, y)))
                continue
            if (a, z, y) not in res and maxcost is not None:
                continue
            if (a, z, y) not in res or res[(a, z, y)][2] != int(f[5]) or res[(a, z, y)][0] != t:
                print("MISMATCH", line.strip(), "ours", res.get((a, z, y)))
                bad += 1
        for k, v in res.items():
            if k not in seen and v[2]:
                print("MISSING IN AUTHOR FILE with P8 tuples", k, v)
                bad += 1
        print(f"# compared with {fn}: {len(seen)} author lines; bad so far = {bad}")
    print("# FAIL" if bad else "# OK")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
