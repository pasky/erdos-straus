"""z38_stats.py: summary of z38_mbm output (n isprime R M0 MBM MBM8) by n mod 8; zeros of R* at non-squares vs main terms."""
import sys, math
rows = [l.split() for l in open(sys.argv[1]) if not l.startswith('#')]
data = [(int(r[0]), int(r[1]), int(r[2]), float(r[3]), float(r[4]), float(r[5])) for r in rows]
only_primes = len(sys.argv) > 2 and sys.argv[2] == 'p'
for cls in (1, 3, 5, 7):
    D = [d for d in data if d[0] % 8 == cls and (d[1] or not only_primes) and math.isqrt(d[0])**2 != d[0]]
    if not D: continue
    N = len(D); z = [d for d in D if d[2] == 0]
    mR = sum(d[2] for d in D)/N; m0 = sum(d[3] for d in D)/N; mb = sum(d[4] for d in D)/N; m8 = sum(d[5] for d in D)/N
    vb = sum((d[2]-d[4])**2 for d in D)/N; v8 = sum((d[2]-d[5])**2 for d in D)/N; v0 = sum((d[2]-d[3])**2 for d in D)/N
    print(f"n≡{cls} (8): N={N} zeros={len(z)} mean R={mR:.2f} M0={m0:.2f} MBM={mb:.2f} MBM8={m8:.2f} | var(R-M)/2M: M0 {v0/2/m0:.2f} MBM {vb/2/mb:.2f} MBM8 {v8/2/m8:.2f}")
    zz = sorted(z, key=lambda d: -d[5]/math.log(d[0])**2)[:6]
    print("   largest MBM8/log^2 among zeros:", [(d[0], d[1], round(d[4], 2), round(d[5], 2), round(d[5]/math.log(d[0])**2, 3)) for d in zz])
sq = [d for d in data if math.isqrt(d[0])**2 == d[0]]
print(f"odd squares: {len(sq)}; max R, MBM, MBM8 there: {max(d[2] for d in sq)}, {max(d[4] for d in sq):.3g}, {max(d[5] for d in sq):.3g}")
