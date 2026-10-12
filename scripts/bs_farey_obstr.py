"""O144 (b): HKRS-style "reciprocity obstruction" census for ES Type I / Type II.

Reads the binary count arrays produced by scripts/spec_typecount.c (FI[n], FII[n], uint32, n <= N)
and reports
  (1) all n <= N (n >= 5) with FI[n] + FII[n] == 0, classified (odd square / other);
  (2) for primes p == 1 (mod 24): distribution of (FI+FII)/log^3 p split by quartic-residue
      invariants that are NOT congruence data: (2/p)_4 and (3/p)_4 (when defined), and the
      Gaussian-prime ratio (p = a^2+b^2) invariants.
Usage: PYTHONPATH=scripts uv run python scripts/bs_farey_obstr.py PREFIX N
"""
import sys, math
import numpy as np

pref, N = sys.argv[1], int(sys.argv[2])
FI = np.fromfile(pref + ".FI.bin", dtype=np.uint32)[: N + 1].astype(np.int64)
FII = np.fromfile(pref + ".FII.bin", dtype=np.uint32)[: N + 1].astype(np.int64)
F = FI + FII

sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i * i :: i] = False

zeros = [n for n in np.nonzero(F == 0)[0] if n >= 5]
sq = [n for n in zeros if math.isqrt(n) ** 2 == n]
other = [n for n in zeros if math.isqrt(n) ** 2 != n]
print(f"N={N}: n>=5 with FI+FII=0: {len(zeros)}; perfect squares {len(sq)}; non-squares {len(other)}")
oddsq_all = [m * m for m in range(3, math.isqrt(N) + 1, 2)]
missing_oddsq = [n for n in oddsq_all if F[n] != 0]
print("odd squares with FI+FII>0 (should be none):", missing_oddsq[:10])
print("even squares among zeros:", [n for n in sq if n % 2 == 0][:20])
print("non-square zeros (first 40):", other[:40])
primes_zero = [n for n in zeros if sieve[n]]
print("primes with FI+FII=0:", primes_zero)

# (2) quartic statistics for p == 1 (mod 24)
def quartic(a, p):  # a^((p-1)/4) mod p in {1,-1, other}; requires p == 1 mod 4 and (a/p)=1
    return pow(a, (p - 1) // 4, p)

ps = np.nonzero(sieve)[0]
ps = ps[(ps % 24 == 1) & (ps > 1000)]
r = F[ps] / np.log(ps.astype(float)) ** 3
rI = FI[ps] / np.log(ps.astype(float)) ** 3
for a in (2, 3):
    # p == 1 mod 24 => (2/p)=(3/p)=1, so quartic symbol is +-1
    q = np.array([quartic(a, int(p)) for p in ps])
    for val, name in ((1, "+1"), (int(ps[0]) and None, None)):
        pass
    plus = q == 1
    print(f"({a}/p)_4: n(+1)={plus.sum()} n(-1)={(~plus).sum()} | "
          f"mean F/L^3 {r[plus].mean():.4f} vs {r[~plus].mean():.4f} | "
          f"mean FI/L^3 {rI[plus].mean():.4f} vs {rI[~plus].mean():.4f} | "
          f"min F/L^3 {r[plus].min():.4f} vs {r[~plus].min():.4f} | "
          f"5%-quantile {np.quantile(r[plus],0.05):.4f} vs {np.quantile(r[~plus],0.05):.4f}")
# control: split by a congruence invariant of the same size, p mod 48
c = (ps % 48) == 1
print(f"control p mod 48 (1 vs 25): mean F/L^3 {r[c].mean():.4f} vs {r[~c].mean():.4f}")
