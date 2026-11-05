# z58 DISPROOF §4.1: matched depression rho per design: mean over the design's primes of (R/L^2)/c0(p), c0 = C0 reference
# (p = 1 (24)) mean R/L^2 interpolated linearly in log10 p between 1e10 (runA/C0) and 1e12 (runB/C0_12); and the
# surviving-mass prediction 0.877 * surv(y,p)/surv(7,p) (MC table survmc_quick.txt, interpolated in log10 p).
import math, glob, sys
def load(fn):
    out = []
    for l in open(fn):
        if l.startswith('#'): continue
        f = l.split()
        if f[8] != '-': out.append((int(f[0]), int(f[8]), int(f[9])))
    return out
def mean(xs): return sum(xs) / len(xs)
c10 = mean([r / math.log(p) ** 2 for p, r, _ in load('data/z58/disproof/runA/C0.txt')])
c12 = mean([r / math.log(p) ** 2 for p, r, _ in load('data/z58/disproof/runB/C0_12.txt')])
c0 = lambda p: c10 + (c12 - c10) * (math.log10(p) - 10) / 2
MC = {}  # y -> {e: surv}
YS = [3, 7, 13, 31, 61, 97, 199, 499, 997]
for l in open('data/z58/disproof/survmc_quick.txt'):
    if l.startswith('p=1e'):
        f = l.split(); e = int(f[0][4:])
        for y, v in zip(YS, f[1:]): MC.setdefault(y, {})[e] = float(v)
def surv(y, p):
    x = math.log10(p); es = sorted(MC[y])
    for a, b in zip(es, es[1:]):
        if a <= x <= b: return MC[y][a] + (MC[y][b] - MC[y][a]) * (x - a) / (b - a)
    return MC[y][es[0]] if x < es[0] else MC[y][es[-1]]
def interp_y(y, p):  # log-linear in y between MC grid points
    if y in MC: return surv(y, p)
    lo = max(t for t in YS if t <= y); hi = min(t for t in YS if t >= y)
    w = (math.log(y) - math.log(lo)) / (math.log(hi) - math.log(lo))
    return surv(lo, p) * (1 - w) + surv(hi, p) * w
designs = [("runA/C0", None), ("runA/CM", None), ("runA/D1a", 7), ("runA/D1b", 13), ("runA/D1c", 16), ("runA/D2", 31),
           ("runB/SM61", 61), ("runB/SM97", 97), ("runB/NSQnear", None), ("runB/NSQfar", None), ("runB/C0_12", None), ("runB/SM31_12", 31)]
print(f"# c0(1e10) = {c10:.4f}, c0(1e12) = {c12:.4f}")
print("# design  n  log10p_range  rho_R  rho_R8  [pred 0.877*surv(y)/surv(7) for square-mimicking designs]")
for name, y in designs:
    d = load(f'data/z58/disproof/{name}.txt')
    rho = mean([r / math.log(p) ** 2 / c0(p) for p, r, _ in d])
    c8 = lambda p: c0(p) * 0.4949   # C0's R8/R ratio at 1e10 (0.0726/0.1467)
    rho8 = mean([r8 / math.log(p) ** 2 / c8(p) for p, _, r8 in d])
    pred = mean([0.877 * interp_y(y, p) / surv(7, p) for p, _, _ in d]) if y else float('nan')
    print(f"{name:14s} {len(d):7d} [{math.log10(d[0][0]):.2f},{math.log10(d[-1][0]):.2f}] {rho:.3f} {rho8:.3f} {pred:.3f}")
