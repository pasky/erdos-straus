"""R240 independent re-summation of the FF_ODD_ABSENCE Thm 2.2 certificate (q = 9, k = 1, P8 = {u0 : u0^4 = -1}).

Own filter (Thm 1.2: 4 | s and eps(s; z, t) = (-1)^{s/4}), own weights mult * 9^{-floor(s/2)} (mult 2 for a < b, 1 for a = b),
own pattern enumeration a <= b, y + t = b. Inputs:
  BOUNDS: output of review_r240_bounds (log of the (J)56 route bound pattern_bound1, every pattern a <= b, s <= 80)
  exact count files from review_r240_enum.py (lines "s a z y t n_all n_P8 lawfail route [..]" or "s a z y t SKIP")
  optionally the author's data/zc/p_20.txt (mode 'author20') for s = 20
  tail (s > 80) and Case A values passed on the command line (re-run by hand, see review).
Fails closed: missing/duplicate patterns, law failures, P8 tuples in incompatible patterns, nonfinite values.
usage: review_r240_certify.py BOUNDS TAIL CASEA ENUMFILE... [--author20 data/zc/p_20.txt]
"""
import sys, math


def eps(s, z, t):
    return (-1) ** ((t + t * z + z * (1 + s) + t * s) % 2)


def die(msg):
    print("FAIL:", msg)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    a20 = None
    if "--author20" in args:
        i = args.index("--author20")
        a20 = args[i + 1]
        del args[i:i + 2]
    bfile, tail, casea, efiles = args[0], float(args[1]), float(args[2]), args[3:]
    bounds = {}
    for l in open(bfile):
        f = l.split()
        s, a, z, y, t = map(int, f[:5])
        if (s, a, z, y) in bounds:
            die("dup bound")
        if not (0 <= a <= s - a - z and y + t == s - a - z and t >= 0):
            die("bad bound pattern " + l)
        bounds[(s, a, z, y)] = (t, float(f[5]))
    exact = {}  # (s,a,z,y) -> n_P8 ; None = SKIP
    for fn in efiles:
        for l in open(fn):
            if l.startswith("#") or l.startswith("exit") or not l.strip():
                continue
            f = l.split()
            s, a, z, y, t = map(int, f[:5])
            if (s, a, z, y) in exact:
                die("dup exact " + l)
            if f[5] == "SKIP":
                exact[(s, a, z, y)] = None
                continue
            n_all, n_p8, lawf = int(f[5]), int(f[6]), int(f[7])
            if lawf:
                die("law failure " + l)
            if n_p8 and (s % 4 or eps(s, z, t) != (-1) ** (s // 4)):
                die("P8 tuple in incompatible pattern " + l)
            exact[(s, a, z, y)] = n_p8
    if a20:
        for l in open(a20):
            f = l.split()
            s, a, z, y, t = map(int, f[:5])
            if (s, a, z, y) in exact and exact[(s, a, z, y)] is not None:
                if f[5] != "SKIP" and int(f[5]) != exact[(s, a, z, y)]:
                    die("author s=20 count differs from ours " + l)
                continue
            exact[(s, a, z, y)] = None if f[5] == "SKIP" else int(f[5])
    per_s = {}
    nb = ne = 0
    for (s, a, z, y), (t, lb) in sorted(bounds.items()):
        if s % 4 or s < 4 or s > 80 or eps(s, z, t) != (-1) ** (s // 4):
            continue
        b = s - a - z
        mult = 2 if a < b else 1
        w = 9.0 ** (-(s // 2))
        n = exact.get((s, a, z, y))
        if n is not None:
            val = mult * n * w
            ne += 1
        else:
            val = mult * math.exp(lb) * w
            nb += 1
        if not math.isfinite(val) or val < 0:
            die("nonfinite")
        per_s.setdefault(s, []).append((val, n is not None))
    # completeness of exact files: every compatible pattern of a level with any exact line must be present (exact or SKIP)
    levels = {k[0] for k in exact}
    for s in levels:
        for (ss, a, z, y), (t, lb) in bounds.items():
            if ss == s and s % 4 == 0 and eps(s, z, t) == (-1) ** (s // 4) and (s, a, z, y) not in exact:
                die(f"level {s}: compatible pattern {(a, z, y, t)} missing from exact files")
    caseB = math.fsum(v for L in per_s.values() for v, _ in L)
    for s in sorted(per_s):
        ex = math.fsum(v for v, e in per_s[s] if e)
        bd = math.fsum(v for v, e in per_s[s] if not e)
        if s <= 28 or s % 20 == 0:
            print(f"s={s}: exact={ex:.6e} bound={bd:.6e}")
    tot = 1.01 * (caseB + tail + casea)
    print(f"caseB(4<=s<=80)={caseB:.10f} ({ne} exact, {nb} route-bounded patterns)  tail={tail}  caseA={casea}")
    print(f"certified total x1.01 = {tot:.6f}  < 4: {tot < 4}")
    sys.exit(0 if tot < 4 else 1)


if __name__ == "__main__":
    main()
