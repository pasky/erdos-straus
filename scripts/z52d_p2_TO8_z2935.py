# z52d P2 TO8 Z2935: failure sets F_t = {n : D^-_t(tn+1)=0}, D^-_t(N)=#{d|N : d = -1 mod t}, t<=64, n<=NMAX.
# Also premise check: t=28, N=141 (D=0), and multiplicative subset-product criterion vs divisor criterion.
import sys, itertools, math
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
TMAX = 64
M = 64 * NMAX + 2
spf = list(range(M + 1))
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def divisors(N):
    f = {}
    while N > 1:
        q = spf[N]; f[q] = f.get(q, 0) + 1; N //= q
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def Dminus(t, N):
    return sum(1 for d in divisors(N) if d % t == t - 1)
print("premise t=28 N=141 divisors mod 28:", [(d, d % 28) for d in divisors(141)], "D=", Dminus(28, 141))
ts = list(range(2, TMAX + 1))
F = {t: [False] * (NMAX + 1) for t in ts}
for t in ts:
    for n in range(1, NMAX + 1):
        F[t][n] = (Dminus(t, t * n + 1) == 0)
dens = {t: sum(F[t][1:]) / NMAX for t in ts}
print("density of failure F_t (n<=%d), t:dens" % NMAX)
print(' '.join(f"{t}:{dens[t]:.4f}" for t in ts))
# pairwise correlation ratios for t, t' with independence baseline
pairs = []
for a, b in itertools.combinations(ts, 2):
    both = sum(1 for n in range(1, NMAX + 1) if F[a][n] and F[b][n])
    exp = dens[a] * dens[b] * NMAX
    if exp > 0: pairs.append((both / exp, a, b, both, round(exp, 1)))
pairs.sort()
print("lowest joint/indep ratios:", [(round(r, 3), a, b) for r, a, b, _, _ in pairs[:8]])
print("highest joint/indep ratios:", [(round(r, 3), a, b) for r, a, b, _, _ in pairs[-8:]])
import statistics
print("median ratio over pairs:", round(statistics.median([p[0] for p in pairs]), 4), "n pairs", len(pairs))
# all-t failure: n with F_t for every t in 2..64 with t | 12 ? (small t sets)
for S in [(3,4,5),(3,5,7,8,11,12),(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64)]:
    ns = [n for n in range(1, NMAX + 1) if all(F[t][n] for t in S)]
    print("n failing at all t in", (S[:6], '...' if len(S)>6 else ''), "count", len(ns), "first", ns[:10])
# multiplicative criterion check: divisor criterion == existence of sub-multiset product == -1 mod t (same set; test on random N)
import random
bad = 0
for N in random.sample(range(2, M - 1), 3000):
    t = random.randint(2, 64)
    if N % t != 1 % t: continue
    f = {}
    x = N
    while x > 1:
        q = spf[x]; f[q] = f.get(q, 0) + 1; x //= q
    primes = [q for q, e in f.items() for _ in range(e)]
    reach = {1}
    for q in primes:
        reach |= {(r * q) % t for r in reach}
    crit = (t - 1) in reach
    if crit != (Dminus(t, N) > 0): bad += 1
print("subset-product vs divisor criterion mismatches:", bad)
