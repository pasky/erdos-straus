# z52d audit A0, item Z3146: multiplicative energy of divisor classes of N_e = (p+e)/4 mod e, e ≤ EMAX, e ≡ 3 (4).
# Normalised energy ratio  rho = E×(D_e) / E_rand(k, φ(e)),  D_e = multiset {d mod e : d | N_e, gcd(d,e)=1}, k = |D_e|,
# E_rand = 2k² − k + k⁴/φ(e) (expected energy of k independent uniform elements; exact for distinct-sum bookkeeping up to
# O(k³/φ)), plus the Type II slice success flag  S_e = [−1 ∈ {a b⁻¹ mod e : ab | N_e}].
# Compare: hardest primes (fewest successful slices) vs typical primes vs random odd integers n ≡ 1 (24) (non-prime).
import math, random, sys
from collections import Counter

EMAX = 1000
LIM = 3_000_000
spf = list(range(LIM // 4 + EMAX + 2))
for i in range(2, int(len(spf) ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, len(spf), i):
            if spf[j] == j: spf[j] = i

def divisors(n):
    fs = Counter()
    while n > 1:
        q = spf[n]; fs[q] += 1; n //= q
    ds = [1]
    for q, a in fs.items():
        ds = [d * q ** k for d in ds for k in range(a + 1)]
    return ds

phi_c = {}
def phi(e):
    if e not in phi_c:
        r, n, q = e, e, 2
        while q * q <= n:
            if n % q == 0:
                r -= r // q
                while n % q == 0: n //= q
            q += 1
        if n > 1: r -= r // n
        phi_c[e] = r
    return phi_c[e]

def slice_stats(n, e):
    N = (n + e) // 4
    ds = divisors(N)
    cls = [d % e for d in ds if math.gcd(d, e) == 1]
    k = len(cls)
    prod = Counter((a * b) % e for a in cls for b in cls)
    E = sum(v * v for v in prod.values())
    Er = 2 * k * k - k + k ** 4 / phi(e)
    dset = set(ds)
    succ = any(math.gcd(a * b, e) == 1 and (a + b) % e == 0 for a in ds for b in ds if a * b <= N and N % (a * b) == 0)
    return E / Er, succ, k

def profile(n):
    rows = [slice_stats(n, e) for e in range(3, EMAX + 1, 4) if (n + e) % 4 == 0]
    return rows

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

random.seed(1)
X0, X1 = 1_000_000, 3_000_000
primes = [p for p in range(X0 + 1, X1, 24) if isprime(p)]
sample = random.sample(primes, 400)
comps = random.sample([n for n in range(X0 + 1, X1, 24) if not isprime(n) and int(math.isqrt(n)) ** 2 != n], 150)
res = {}
for n in sample + comps:
    rows = profile(n)
    res[n] = rows
def summ(ns):
    lr = [math.log(r) for n in ns for r, s, k in res[n]]
    return sum(lr) / len(lr)
succ_count = {p: sum(s for r, s, k in res[p]) for p in sample}
order = sorted(sample, key=lambda p: succ_count[p])
hard, typ = order[:40], order[160:240]
print(f"slices per n: {len(res[sample[0]])}; succ count: min {succ_count[order[0]]} median {succ_count[order[200]]} max {succ_count[order[-1]]}")
print(f"mean log rho: hardest-40 primes {summ(hard):.4f}  typical primes {summ(typ):.4f}  all primes {summ(sample):.4f}  composites {summ(comps):.4f}")
# within-prime: energy ratio on failing vs successful slices
f_lr = [math.log(r) for p in sample for r, s, k in res[p] if not s]
s_lr = [math.log(r) for p in sample for r, s, k in res[p] if s]
print(f"mean log rho on failing slices {sum(f_lr)/len(f_lr):.4f} (n={len(f_lr)}) vs successful {sum(s_lr)/len(s_lr):.4f} (n={len(s_lr)})")
# control for slice size k: bucket by tau and compare failing/successful within bucket
import collections
b = collections.defaultdict(lambda: [[], []])
for p in sample:
    for r, s, k in res[p]:
        b[k][s].append(math.log(r))
tot_w = 0; acc = 0
for k in sorted(b):
    F, S = b[k]
    if len(F) >= 20 and len(S) >= 20:
        d = sum(F)/len(F) - sum(S)/len(S); w = min(len(F), len(S)); acc += d*w; tot_w += w
        print(f"  k={k:3d}: fail n={len(F):5d} mean {sum(F)/len(F):+.3f} | succ n={len(S):5d} mean {sum(S)/len(S):+.3f} | diff {d:+.3f}")
print(f"k-stratified weighted mean diff (fail - succ) in log rho: {acc/tot_w:+.4f}")
print("hardest primes and their success counts:", [(p, succ_count[p]) for p in hard[:10]])
# control for e as well: stratify by (k, e-bucket of width 100); also test the character-trapping explanation:
# fraction of failing slices whose classes all lie in the kernel of some odd character mod e (=> -1 not a ratio, exact).
b2 = collections.defaultdict(lambda: [[], []])
for p in sample:
    es = [e for e in range(3, EMAX + 1, 4) if (p + e) % 4 == 0]
    for e, (r, s, k) in zip(es, res[p]):
        b2[(k, e // 100)][s].append(math.log(r))
acc = tw = 0
for key, (F, S) in b2.items():
    if len(F) >= 10 and len(S) >= 10:
        w = min(len(F), len(S)); acc += (sum(F)/len(F) - sum(S)/len(S)) * w; tw += w
print(f"(k, e//100)-stratified weighted diff (fail - succ): {acc/tw:+.4f}")
def subgroup_gen(gens, e):
    H = {1}; frontier = [1]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = x * g % e
            if y not in H: H.add(y); frontier.append(y)
    return H
trap = tot = 0; trap_s = tot_s = 0
for p in sample[:150]:
    es = [e for e in range(3, EMAX + 1, 4) if (p + e) % 4 == 0]
    for e, (r, s, k) in zip(es, res[p]):
        N = (p + e) // 4
        cls = [d % e for d in divisors(N) if math.gcd(d, e) == 1]
        H = subgroup_gen(set(cls), e)
        if s: tot_s += 1; trap_s += (e - 1) in H
        else: tot += 1; trap += (e - 1) not in H
print(f"failing slices with -1 outside the subgroup generated by the divisor classes: {trap}/{tot} = {trap/tot:.3f}; successful slices with -1 inside: {trap_s}/{tot_s}")
