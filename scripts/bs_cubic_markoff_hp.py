"""O143 memo 2: Markoff class numbers h(k) (Ghosh-Sarnak fundamental sets) vs local densities.

For 5 < k <= K: h+(k) = #{3 <= u1 <= u2 <= u3 : u1^2+u2^2+u3^2+u1u2u3 = k} (GS Thm 1.1(i)).
Admissible: k != 3 (mod 4), k != +-3 (mod 9) (GS Prop 6.1, quoted from memory -> we also check
local solvability mod 8, 9 and mod primes <= 50 directly).  Exceptional (GS): k = u^2+v^2, 4(k-1) = u^2+3v^2,
k = 4+u^2 (these have a point with |x_j| in {0,1,2}).
Hasse failure := admissible, not exceptional, h+(k) = 0.
Then: does the truncated singular series S(k) = prod_{l<=L} #V_k(Z/l)/l^2 separate failures from successes?
Run: PYTHONPATH=scripts uv run python scripts/bs_cubic_markoff_hp.py [K]
"""
import sys
import numpy as np
from math import isqrt, log

K = int(sys.argv[1]) if len(sys.argv) > 1 else 200000

h = np.zeros(K + 1, dtype=np.int64)
u1 = 3
while 3*u1*u1 + u1**3 <= K:
    u2 = u1
    while u1*u1 + 2*u2*u2 + u1*u2*u2 <= K:
        u3 = np.arange(u2, K, dtype=np.int64)
        base = u1*u1 + u2*u2
        # u3 range: u3^2 + u1u2u3 + base <= K
        disc = (u1*u2)**2 - 4*(base - K)
        u3max = int((-(u1*u2) + isqrt(disc))//2) + 1
        u3 = np.arange(u2, u3max + 1, dtype=np.int64)
        kv = base + u3*u3 + u1*u2*u3
        kv = kv[kv <= K]
        np.add.at(h, kv, 1)
        u2 += 1
    u1 += 1

# local counts mod m for m in MODS: N_m[r] = #{x mod m : M(x) = r}
def local_table(m):
    x = np.arange(m)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    v = (X*X + Y*Y + Z*Z - X*Y*Z) % m
    return np.bincount(v.ravel(), minlength=m)

MODS = [8, 9, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
tabs = {m: local_table(m) for m in MODS}
ks = np.arange(K + 1)
admissible = np.ones(K + 1, bool)
logS = np.zeros(K + 1)
for m in MODS:
    cnt = tabs[m][ks % m]
    admissible &= cnt > 0
    # density relative to m^2 (dimension 2)
    logS += np.log(np.maximum(cnt, 1) / m**2)

exc = np.zeros(K + 1, bool)
for u in range(0, isqrt(K) + 1):
    for v in range(u, isqrt(K - u*u) + 1):
        exc[u*u + v*v] = True
    if 4 + u*u <= K:
        exc[4 + u*u] = True
for u in range(0, 2*isqrt(K) + 2):
    for v in range(0, isqrt(4*K // 3) + 2):
        t = u*u + 3*v*v
        if t % 4 == 0 and t//4 + 1 <= K:
            exc[t//4 + 1] = True

gen = admissible & ~exc
gen[:6] = False
fail = gen & (h == 0)
print(f"K={K}: admissible {admissible[1:].sum()}, admissible generic {gen.sum()}, Hasse failures {fail.sum()} = {100*fail.sum()/admissible[1:].sum():.2f}% of admissible; at k<=100800: {100*fail[:100801].sum()/admissible[1:100801].sum():.2f}%")
for lo in [K//8, K//4, K//2]:
    sl = slice(lo, 2*lo)
    g = gen[sl]
    hh = h[sl][g]
    L2 = log(1.5*lo)**2
    print(f"  k in [{lo},{2*lo}): generic {g.sum()}, failures {fail[sl].sum()}, mean h {hh.mean():.2f}, "
          f"mean h/log^2k {hh.mean()/L2:.3f}, frac h<=1: {(hh<=1).mean():.4f}, max h {hh.max()}")
# singular-series separation on the top dyadic range
lo = K//2
sl = slice(lo, K + 1)
g = gen[sl]
S = np.exp(logS[sl][g]); hh = h[sl][g]
qs = np.quantile(S, [0.1, 0.25, 0.5, 0.75, 0.9])
print("  truncated singular series S(k) quantiles (generic, top range):", np.round(qs, 3))
for a, b in zip([0] + list(qs), list(qs) + [np.inf]):
    m = (S >= a) & (S < b)
    print(f"   S in [{a:.3f},{b:.3f}): n={m.sum()}, failure rate {(hh[m]==0).mean():.4f}, mean h {hh[m].mean():.2f}")
corr = np.corrcoef(np.log(S), np.log1p(hh))[0, 1]
print(f"  corr(log S, log(1+h)) = {corr:.3f}")
