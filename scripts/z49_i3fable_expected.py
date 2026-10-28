"""z49_i3fable_expected.py — expected number of zeros of I3 beyond X, by local type, from the CRT-model grid
(data/z49_i3fable/crt_grid/N*_<type>.txt) and the census (data/z48_ltfable/big_1e9.txt).
log P is interpolated linearly in log N between grid points; where the tail pass had no survivors (P reported 0)
we use the conservative estimate P1 * P2_last (P2 from the largest N with a nonzero tail count, which overstates P
since P2 decreases with N).  Beyond the last grid point, P is extrapolated with the last log-log slope.
Usage: uv run python scripts/z49_i3fable_expected.py
"""
import glob, re, math, os

TYPES = {"sq_2-0": ("even squares", lambda n: 1 / (4 * math.sqrt(n))), "sq_2-1": ("odd squares", lambda n: 1 / (4 * math.sqrt(n))),
         "sq2": ("2*square", lambda n: 1 / (2 * math.sqrt(2 * n))), "gen_2-0": ("even non-square", lambda n: 0.5), "gen_2-1": ("odd non-square", lambda n: 0.5)}

def load():
    out = {}
    for f in glob.glob("data/z49_i3fable/crt_grid/N*_*.txt"):
        m = re.match(r".*/N(\d+)_(.*)\.txt", f); N = int(m.group(1)); typ = m.group(2)
        txt = open(f).read()
        p1 = re.search(r"P1\(X0=\d+\)=([0-9.e+-]+)", txt); tail = re.search(r"tail: (\d+) of (\d+) survivors", txt)
        if not p1 or not tail: continue
        out.setdefault(typ, {})[N] = (float(p1.group(1)), int(tail.group(1)), int(tail.group(2)))
    return out

def main():
    data = load()
    zeros = [int(l.split()[1]) for l in open("data/z48_ltfable/big_1e9.txt") if l.startswith("I30")]
    def ztype(n):
        r = math.isqrt(n)
        if r * r == n: return "sq_2-0" if n % 2 == 0 else "sq_2-1"
        if n % 2 == 0:
            r2 = math.isqrt(n // 2)
            if 2 * r2 * r2 == n: return "sq2"
            return "gen_2-0"
        return "gen_2-1"
    curves = {}
    print("# model P(I3(n)=0) by type and nominal N  (P1 = no word with larger endpoint <= sqrt N; P2 = tail; * = P2 borrowed from last nonzero tail)")
    for typ, (name, dens) in TYPES.items():
        pts = sorted(data.get(typ, {}).items())
        last_p2 = None; curve = []
        for N, (p1, a, b) in pts:
            if a > 0: last_p2 = a / b; p = p1 * a / b; flag = ""
            else: p = p1 * (last_p2 if last_p2 else 1.0); flag = "*"
            curve.append((N, p)); print(f"{name:18s} N={N:>11d}  P1={p1:.3e}  tail={a}/{b}  P={p:.3e}{flag}")
        curves[typ] = curve
    def logP(typ, n):
        c = curves[typ]; x = math.log(n)
        xs = [math.log(N) for N, _ in c]; ys = [math.log(p) if p > 0 else -60 for _, p in c]
        if x <= xs[0]: return ys[0]
        for i in range(1, len(xs)):
            if x <= xs[i]: return ys[i - 1] + (ys[i] - ys[i - 1]) * (x - xs[i - 1]) / (xs[i - 1 + 1] - xs[i - 1])
        return ys[-1] + (ys[-1] - ys[-2]) * (x - xs[-1]) / (xs[-1] - xs[-2])
    def expected(typ, a, b, steps=4000):
        # integral of density * P over [a, b] in log n
        la, lb = math.log(a), math.log(b); s = 0.0
        for i in range(steps):
            x = la + (lb - la) * (i + 0.5) / steps; n = math.exp(x)
            s += TYPES[typ][1](n) * math.exp(logP(typ, n)) * n * (lb - la) / steps
        return s
    print("\n# expected number of zeros in (X, 1e9] (model) vs census, by type; last column: model expectation beyond 1e9 (extrapolated)")
    for X in [1000, 3000, 10000, 36078, 100000, 1000000, 2433600, 10000000, 100000000]:
        row = []; tot = 0.0; totc = 0
        for typ, (name, _) in TYPES.items():
            e = expected(typ, X, 1e9); c = sum(1 for z in zeros if z > X and ztype(z) == typ); tot += e; totc += c
            row.append(f"{name}: {e:.2f} (census {c})")
        print(f"X={X:>10d}: total model {tot:.2f} vs census {totc:3d} | " + "; ".join(row))
    beyond = {typ: expected(typ, 1e9, 1e13) for typ in TYPES}
    print("\n# model expectation of zeros in (1e9, 1e13]: " + ", ".join(f"{TYPES[t][0]} {beyond[t]:.2e}" for t in TYPES))

if __name__ == "__main__":
    main()
