"""R88 from-scratch toy checks for EXCEPTIONAL_SHORT.md (not reusing author code).

1. lem:identity (multiplier identity) on random small parameters, exact rationals.
2. Toy LL-atom family + selector + even Bonferroni Q_r: build nu(n) pointwise on one
   period M, compute exact E nu, then check |sum_{n in I} nu(n) - H E nu| <= T_abs on
   random real windows I=(z,z+H] (Lemma 1.1, shift uniformity), including max over shifts.
3. Lemma 2.1: Q with all primes > max prime of M  =>  E[nu 1_{beta (Q)}] = E nu / Q.
4. Remark 2.2 adversarial: E[nu | n = 0 mod p] for primes p | L_K vs E nu.
5. Lemma 1.2(b) chain + (c) Rankin inequality numerically.
"""
import math, random, itertools
from fractions import Fraction
import numpy as np

random.seed(88)

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

# ---- 1. identity
bad = 0
for _ in range(3000):
    k = random.choice(range(1, 60, 4)); l = random.choice([p for p in primes_upto(400) if p > 3])
    if (k * l) % 4 != 3: continue
    A = (k * l + 1) // 4
    divs = [d for d in range(1, A + 1) if A % d == 0]
    u = random.choice(divs); rest = A // u
    v = random.choice([d for d in divs if rest % d == 0]); w = rest // v
    vinv = pow(v, -1, k * l); a = (-u * vinv) % (k * l)
    for n in range(a if a else k * l, a + 20 * k * l, k * l):
        if n < 1: continue
        s = (n * v + u) // (k * l)
        assert (n * v + u) % (k * l) == 0 and s >= 1
        if Fraction(4, n) != Fraction(1, s*u*w) + Fraction(1, n*s*v*w) + Fraction(1, n*u*v*w):
            bad += 1
print("1. identity failures:", bad)

# ---- 2. toy family
K = 5; ks = [k for k in range(1, K + 1) if k % 4 == 1]   # {1,5}
ells = [p for p in primes_upto(32) if p > 7 and p % 4 == 3]
atoms = []
for k in ks:
    for l in ells:
        A = (k * l + 1)
        for u in range(1, 8):
            for v in range(1, 8):
                if math.gcd(u, v) == 1 and math.gcd(u * v, k) == 1 and A % (4 * u * v) == 0 and u*v>1:
                    atoms.append((k * l, (-u * pow(v, -1, k * l)) % (k * l)))
atoms = sorted(set(atoms))
y = 3; Py = 6
LK = 1
for k in ks: LK = LK * k // math.gcd(LK, k)
M = LK * Py // math.gcd(LK, Py)
for l in sorted({m for m, _ in atoms}):
    M = M * l // math.gcd(M, l)
print("2. atoms:", len(atoms), "moduli:", sorted({m for m,_ in atoms}), "M =", M)
assert M <= 3 * 10**7
r = 2
n = np.arange(M, dtype=np.int64)
Hc = np.zeros(M, dtype=np.int32)
for m, a in atoms:
    Hc[a::m] += 1
Q = np.zeros(M, dtype=np.int64)
for j in range(r + 1):
    Q += (-1) ** j * np.array([math.comb(int(h), j) for h in range(Hc.max() + 1)])[Hc]
S = (np.gcd(n, Py) == 1).astype(np.int64)
nu = S * Q
assert nu.min() >= 0
Enu = Fraction(int(nu.sum()), M)
Tabs = 2 ** len(primes_upto(y)) * sum(math.comb(len(atoms), j) for j in range(r + 1))
print("   E nu =", float(Enu), " P(H=0,S=1) =", float(((Hc == 0) & (S == 1)).mean()), " T_abs =", Tabs)
pref = np.concatenate([[0], np.cumsum(np.concatenate([nu, nu]))])
def window(z, H):  # sum over integers n in (z, z+H], z real, via periodicity
    lo = math.floor(z) + 1; hi = math.floor(z + H)
    tot = 0; cnt = hi - lo + 1
    q, rem = divmod(cnt, M); tot += q * int(nu.sum())
    s = lo % M
    tot += int(pref[s + rem] - pref[s])
    return tot
worst = 0.0
for _ in range(20000):
    H = random.choice([10, 100, 1000, 10**4, 10**5, 10**6, 10**8]) * random.random() + 1
    z = random.uniform(-1e12, 1e12)
    dev = abs(window(z, H) - H * float(Enu))
    worst = max(worst, dev / Tabs)
print("   max |sum - H E nu| / T_abs over random windows:", round(worst, 4), "(must be <= 1)")
# max over all shifts for fixed H
for H in (50, 500, 5000):
    sums = pref[H:M + H] - pref[:M]
    print(f"   H={H}: max_z sum = {sums.max()}, H*Enu = {H*float(Enu):.1f}, bound H*Enu+T_abs = {H*float(Enu)+Tabs:.1f}")

# ---- 3. Lemma 2.1
Pmax = max(p for p in primes_upto(100) if M % p == 0)
for Qm in (61, 67 * 71):
    for beta in (0, 1, 17):
        idx = (beta + Qm * np.arange(M, dtype=np.int64)) % M  # n = beta + Q j, j over a period
        val = Fraction(int(nu[idx].sum()), M * Qm)
        assert val == Enu / Qm, (Qm, beta)
print("3. Lemma 2.1 independence exact for Q in {61, 67*71} (primes >", Pmax, ")")

# ---- 4. adversarial smooth conditioning
for p in (5,):
    print(f"4. E[nu | n=0 mod {p}] = {float(Fraction(int(nu[::p].sum()), M//p)):.4f} vs E nu = {float(Enu):.4f}")
for p in ells[:3]:
    vals = [float(Fraction(int(nu[b::p].sum()), M // p)) for b in range(p)]
    print(f"   p={p}: E[nu | n=b mod p] ranges {min(vals):.4f}..{max(vals):.4f}; ratio max/E = {max(vals)/float(Enu):.2f} (<= p)")

# ---- 5. Lemma 1.2(b),(c)
for _ in range(2000):
    yy = random.choice([5, 7, 13, 29]); ps = primes_upto(yy)
    d = 1
    while d < 10**6: d *= random.choice(ps)
    D0 = random.randint(1, d - 1)
    chain = [d]; x = d
    while x > 1:
        p = max(q for q in ps if x % q == 0); x //= p; chain.append(x)
    dp = [c for c in chain if c > D0][-1]
    assert D0 < dp <= yy * D0 and d % dp == 0
u = 2 ** -0.5; assert -math.log(1 - u) <= 2 * u
for yy in (10, 100, 1000, 10**5):
    assert sum(p ** -0.5 for p in primes_upto(yy)) <= 2 * math.sqrt(yy)
# Rankin explicit check for y=13, D0 = 10^4
yy = 13; ps = primes_upto(yy); D0 = 10**4
def smooth_upto(N):
    out = [1]
    for p in ps:
        out = [a * p**e for a in out for e in range(0, int(math.log(N, p)) + 1) if a * p**e <= N]
    return out
lhs = sum(1 / d for d in smooth_upto(10**12) if d > D0)
rhs = D0 ** -0.5 * math.prod(1 / (1 - p ** -0.5) for p in ps)
print(f"5. chain lemma ok; Rankin y=13,D0=1e4: sum_(D0,1e12] 1/d = {lhs:.4g} <= {rhs:.4g} <= e^(4 sqrt y)/sqrt(D0) = {math.exp(4*math.sqrt(yy))/100:.4g}")
