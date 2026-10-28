"""z49_i3fable_stats.py — test the local-density model E[I3(n)] ≈ S_div(n) * S_gen(n) * M0(n) on the exact counts.
M0(n) = sum_{t,u>=3, u(3t-1)<=n+3} 1/(tu-1) (exact main term, tabulated+interpolated in log n),
S_div(n) = prod_{l|n} (1-(l-1)/l^2) * prod_{l∤n} (1+1/l^2) = (zeta(2)/zeta(4)) * prod_{l|n} (l^2-l+1)/(l^2+1),
S_gen(n) = 1/2 if n is a square, 2/3 if n = 2*square, else 1 (first-order genus prediction; levels with k | 2t only).
Usage: uv run python scripts/z49_i3fable_stats.py PREFIX LO HI
"""
import sys, numpy as np
from math import log, isqrt

def M0_exact(n):
    s = 0.0; t = 3
    while 3 * (3 * t - 1) <= n + 3:
        U = (n + 3) // (3 * t - 1)
        u = np.arange(3, U + 1, dtype=np.float64)
        s += float(np.sum(1.0 / (t * u - 1.0)))
        t += 1
    return s

def main():
    prefix, LO, HI = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    I3 = np.fromfile(prefix + "_i3.u16", dtype=np.uint16).astype(np.float64)
    N = len(I3) - 1
    n = np.arange(N + 1, dtype=np.int64)
    # M0 by interpolation in log n (M0 is smooth); exact at 60 log-spaced points
    grid = np.unique(np.round(np.exp(np.linspace(log(max(LO, 100)), log(HI), 60))).astype(np.int64))
    M0g = np.array([M0_exact(int(g)) for g in grid])
    M0 = np.zeros(N + 1); sel = n >= max(LO, 100)
    M0[sel] = np.interp(np.log(n[sel]), np.log(grid), M0g)
    # S_div via smallest-prime-factor sieve of the ratio prod_{l|n} (l^2-l+1)/(l^2+1)
    Z = 1.5198177; Sdiv = np.full(N + 1, Z)
    spf_done = np.zeros(N + 1, dtype=bool)
    for l in range(2, N + 1):
        if spf_done[l]: continue
        # l is prime (not marked by smaller primes)
        Sdiv[l::l] *= (l * l - l + 1) / (l * l + 1)
        if l * l <= N: spf_done[l * l::l] = True
        spf_done[l] = True
    # classes
    sq = np.zeros(N + 1, dtype=bool); r = np.arange(isqrt(N) + 1); sq[r * r] = True
    sq2 = np.zeros(N + 1, dtype=bool); r2 = r[2 * r * r <= N]; sq2[2 * r2 * r2] = True
    isprime = np.ones(N + 1, dtype=bool); isprime[:2] = False
    for l in range(2, isqrt(N) + 1):
        if isprime[l]: isprime[l * l::l] = False
    win = (n >= LO) & (n <= HI)
    odd = (n % 2 == 1)
    classes = [
        ("primes", win & isprime), ("primes 1 mod 4", win & isprime & (n % 4 == 1)),
        ("odd non-square", win & odd & ~sq), ("odd square", win & odd & sq),
        ("even non-square, not 2sq", win & ~odd & ~sq & ~sq2), ("even square", win & ~odd & sq),
        ("2*square", win & sq2), ("n=0 mod 4 non-square", win & (n % 4 == 0) & ~sq),
        ("n=2 mod 4 non-sq non-2sq", win & (n % 4 == 2) & ~sq & ~sq2),
        ("odd, 3|n, non-sq", win & odd & (n % 3 == 0) & ~sq), ("odd, 15|n, non-sq", win & odd & (n % 15 == 0) & ~sq),
        ("odd, gcd(n,210)=1 non-sq", win & odd & (n % 3 != 0) & (n % 5 != 0) & (n % 7 != 0) & ~sq),
        ("even, 30|n non-sq", win & (n % 30 == 0) & ~sq), ("even, 2310|n non-sq", win & (n % 2310 == 0) & ~sq),
        ("all", win),
    ]
    print(f"# window [{LO},{HI}], N={N}; columns: count, mean I3, mean I3/M0, mean I3/(Sdiv*M0), mean Sdiv, min I3, #zeros, sat-frac")
    for name, mask in classes:
        c = int(mask.sum())
        if c == 0: continue
        x = I3[mask]; m0 = M0[mask]; sd = Sdiv[mask]
        print(f"{name:28s} {c:8d} {x.mean():8.2f} {np.mean(x / m0):7.4f} {np.mean(x / (sd * m0)):7.4f} {sd.mean():6.3f} {int(x.min()):5d} {int((x == 0).sum()):4d} {np.mean(x >= 65535):.1e}")
    # by squarefree kernel k: n = k m^2, k <= 15, kernel via sieve on the window only
    print("\n# n = k*m^2 (k squarefree), window: count, mean I3/(Sdiv*M0); prediction 1 - w_k/2 with w_k = log-share of levels with k | 2t")
    for k in [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 21, 30]:
        m = np.arange(1, isqrt(HI // k) + 1); nn = k * m * m; nn = nn[(nn >= LO) & (nn <= HI)]
        if len(nn) == 0: continue
        x = I3[nn]; ratio = np.mean(x / (Sdiv[nn] * M0[nn]))
        print(f"k={k:3d} count={len(nn):6d} ratio={ratio:7.4f}")

if __name__ == "__main__":
    main()
