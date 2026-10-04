"""EXCEPTIONAL_TWIN3 Lemma 3.2 check: second moments of the short sums
r(c) = sum_{v^2 t = c (j), v,t<=Y} 1/(vt) and r1(rho) = sum_{(u,v)=1, u = rho v (j)} 1/(uv).
Prints diagonal, off-diagonal, total, and the random prediction (sum)^2/j.
Usage: uv run --with numpy python scripts/twin3_short_sums.py Y j1 j2 ..."""
import sys, math
import numpy as np

def second_moments(Y, j):
    v = np.arange(1, Y + 1, dtype=np.int64)
    v = v[v % j != 0]
    w = 1.0 / v
    # r(c): accumulate over v (outer loop) with vectorised t
    r = np.zeros(j)
    t = v; wt = w
    for vv, wv in zip(v, w):
        c = (vv * vv % j) * (t % j) % j
        r += np.bincount(c, weights=wv * wt, minlength=j)
    # diagonal for r: same integer N = v^2 t
    # (computed exactly by grouping N)
    Ns = {}
    for vv in v:
        for tt in v:
            N = int(vv) * int(vv) * int(tt)
            Ns[N] = Ns.get(N, 0.0) + 1.0 / (vv * tt)
    diag_r = sum(x * x for x in Ns.values())
    # r1(rho): coprime pairs
    r1 = np.zeros(j); diag1 = 0.0
    for uu, wu in zip(v, w):
        g = np.gcd(uu, v); m = g == 1
        vin = v[m]
        rho = (uu % j) * np.array([pow(int(x), -1, j) for x in vin % j]) % j
        r1 += np.bincount(rho, weights=wu * w[m], minlength=j)
        diag1 += float(np.sum((wu * w[m]) ** 2))
    S = float(r.sum()); S1 = float(r1.sum())
    return dict(sumr=S, tot=float((r * r).sum()), diag=diag_r, rand=S * S / j,
                sumr1=S1, tot1=float((r1 * r1).sum()), diag1=diag1, rand1=S1 * S1 / j)

if __name__ == "__main__":
    Y = int(float(sys.argv[1]))
    print(f"Y={Y}  (bounds: diag_r <= zeta2^2 zeta3^2 = {(math.pi**2/6)**2*1.2020569**2:.3f}, diag_r1 <= zeta2^2 = {(math.pi**2/6)**2:.3f})")
    print("j | sum r | tot r^2 | diag | off | rand || sum r1 | tot r1^2 | diag1 | off1 | rand1")
    for j in map(int, sys.argv[2:]):
        d = second_moments(Y, j)
        print(f"{j} | {d['sumr']:.2f} | {d['tot']:.4f} | {d['diag']:.4f} | {d['tot']-d['diag']:.5f} | {d['rand']:.5f} || "
              f"{d['sumr1']:.2f} | {d['tot1']:.4f} | {d['diag1']:.4f} | {d['tot1']-d['diag1']:.5f} | {d['rand1']:.5f}")
