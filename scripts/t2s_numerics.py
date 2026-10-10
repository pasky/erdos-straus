"""O128 step 3: statistics of f_II(p) for primes p <= N from the output of t2s_count.c.

Usage: t2s_numerics.py BINFILE N
Prints: dyadic minima of f_II, f_II/log^3 p, the d=1 and c=1 subfamilies; the smallest normalised
values; class means by p mod 24 and mod 840; ratio f_II(p) / (mean over primes q ≡ p mod 840 in the
same dyadic block) — an empirical 'singular series' normalisation.
"""
import sys, math
import numpy as np

fn, N = sys.argv[1], int(sys.argv[2])
arr = np.fromfile(fn, dtype=np.uint32).reshape(3, N + 1)
tot, d1, c1 = arr[0], arr[1], arr[2]  # uint32 views (memory)

sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for q in range(2, int(N ** 0.5) + 1):
    if sieve[q]:
        sieve[q * q::q] = False
P = np.nonzero(sieve)[0]
P = P[P >= 5]
f = tot[P].astype(np.int64); L3 = np.log(P.astype(float)) ** 3
norm = f / L3
print(f"primes 5..{N}: {len(P)};  f_II(p) = 0 for {int((f == 0).sum())} primes")
print("\n== dyadic blocks [2^k, 2^{k+1}) ==")
print(" k   #p     min f_II (at p)        max      mean f/log^3  min f/log^3 (at p)   #d1=0   #c1=0  min d1  min c1")
for k in range(3, int(math.log2(N)) + 1):
    m = (P >= 2 ** k) & (P < 2 ** (k + 1))
    if not m.any():
        continue
    Pk, fk, nk = P[m], f[m], norm[m]
    i, j = int(np.argmin(fk)), int(np.argmin(nk))
    print(f"{k:2d} {m.sum():8d} {fk[i]:6d} ({Pk[i]:9d}) {fk.max():7d}   {nk.mean():.4f}     {nk[j]:.4f} ({Pk[j]:9d})"
          f"  {int((d1[Pk] == 0).sum()):7d} {int((c1[Pk] == 0).sum()):7d} {d1[Pk].min():5d} {c1[Pk].min():5d}")

print("\n== smallest f_II/log^3 p among p >= 10^5 (20 smallest) ==")
big = P >= 10 ** 5
order = np.argsort(norm[big])[:20]
for t in order:
    p = int(P[big][t])
    print(f"  p={p:9d}  f_II={tot[p]:5d}  f/log^3={norm[big][t]:.4f}  d1={d1[p]:4d} c1={c1[p]:4d}"
          f"  p%24={p % 24:2d} p%840={p % 840:3d}")

print("\n== class means of f_II/log^3 p by p mod 24 (p >= 10^5) ==")
for r in sorted(set((P[big] % 24).tolist())):
    m = big & (P % 24 == r)
    print(f"  {r:2d}: mean {norm[m].mean():.4f}  min {norm[m].min():.4f}  n={m.sum()}")

# empirical singular series: mean of f_II over primes in the same class mod 840 and same dyadic block
W = 840
blk = np.floor(np.log2(P)).astype(int)
key = blk * W + (P % W)
uk, inv = np.unique(key, return_inverse=True)
s = np.bincount(inv, weights=f.astype(float)); cnt = np.bincount(inv)
mean_cls = (s / cnt)[inv]
ratio = f / mean_cls
print(f"\n== ratio R(p) = f_II(p) / mean(f_II over q ≡ p mod {W}, same dyadic block) ==")
for k in range(10, int(math.log2(N)) + 1):
    m = (blk == k) & (cnt[inv] >= 30)
    if not m.any():
        continue
    r = ratio[m]
    j = int(np.argmin(r))
    print(f"  k={k:2d}: min R = {r[j]:.3f} at p={P[m][j]}, 0.1% quantile {np.quantile(r, 0.001):.3f},"
          f" 1% {np.quantile(r, 0.01):.3f}, sd {r.std():.3f}")

print("\n== class mean of f_II/log^3 p by p mod 840 (top block, 8 smallest classes) ==")
kmax = int(math.log2(N)) - 1
m = blk == kmax
cls = {}
for p, v in zip(P[m], norm[m]):
    cls.setdefault(int(p % W), []).append(v)
items = sorted((np.mean(v), r, len(v)) for r, v in cls.items())
for mu, r, n in items[:8]:
    print(f"  p≡{r:3d} (840): mean {mu:.4f} (n={n})")
print(f"  largest: p≡{items[-1][1]} mean {items[-1][0]:.4f}")
