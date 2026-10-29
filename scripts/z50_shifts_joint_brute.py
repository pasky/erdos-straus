# Independent brute-force check of z50_shifts_joint.c on small N.
# Prints the same table format (per class mod 8: v, inC, marginal fail fraction, J(V)/count).
import sys
N = int(sys.argv[1]); VMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40

def divisors(m):
    ds = []
    d = 1
    while d * d <= m:
        if m % d == 0:
            ds.append(d)
            if d * d != m:
                ds.append(m // d)
        d += 1
    return ds

for cls in (1, 5):
    ns = list(range(cls, N + 1, 8))
    mf = [0] * (VMAX + 1); J = [0] * (VMAX + 1)
    for n in ns:
        first = VMAX + 1
        for v in range(3, VMAX + 1):
            inC = (v % 4 == 0) or (v % 2 == 1 and (n + v) % 8 == 0)
            if not inC:
                continue
            h = any((d + 1) % v == 0 for d in divisors(n + v))
            if not h:
                mf[v] += 1
            elif v < first:
                first = v
        for V in range(3, min(first, VMAX + 1)):
            J[V] += 1
    print(f"# class {cls}")
    for v in range(3, VMAX + 1):
        inC = (v % 4 == 0) or (v % 2 == 1 and (cls + v) % 8 == 0)
        print(v, int(inC), "%.6g" % (mf[v] / len(ns) if inC else -1.0), "%.6g" % (J[v] / len(ns)))
