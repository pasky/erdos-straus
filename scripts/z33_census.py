"""O263 §7 census. For n = primes p ≡ 1 (4), 5 ≤ p ≤ X (and odd squares as T1 control), b = 1 line in the d-coordinate
(N = n + 4d, need divisor ≡ −1 mod 4d), levels d ≤ D. Tiers per level:
  F_B : forced (Prop 3.2): small part s = B-smooth part, opaque cofactor L: −1 ∈ Σ(s) ∪ Σ(s)[L]
  A   : actual: −1 ∈ Σ(all prime factors)
  Gen : cap relaxation: −1 ∈ <prime factors> (generated subgroup)
X2 tier (exponent-2 levels, actual factorisation): b=1 d∈{1,2,3,6} (d-coord), c∈{1,2,3,6} (c-coord: cn+1 has divisor ≡ −1 mod 4c),
e = 3 signed slices: Type II N=(n+3)/4, Type I N=(3n+1)/4: need a,b | N, ab | N, a ≡ −b (mod 3).
Each A-certificate at a level is converted to an ES solution and verified exactly (4/n = 1/x+1/y+1/z).
Usage: z33_census.py X D"""
import sys, numpy as np
from fractions import Fraction
X = int(sys.argv[1]); D = int(sys.argv[2])
LIM = 6 * X + 10
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, int(LIM ** 0.5) + 1):
    if spf[i] == 0:
        blk = spf[i * i::i]; m = blk == 0; blk[m] = i; spf[i * i::i] = blk
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx  # primes (and 0,1)
spf = spf.tolist()

def factors(n):
    out = []
    while n > 1:
        q = spf[n]; out.append(q); n //= q
    return out

def sigma(fs, t, start=frozenset([1])):
    S = set(start)
    for f in fs:
        r = f % t
        S |= {x * r % t for x in S}
    return S

def gen_has(fs, t, target):
    S = {1}; frontier = [1]; rs = {f % t for f in fs}
    while frontier:
        nf = []
        for x in frontier:
            for r in rs:
                y = x * r % t
                if y not in S: S.add(y); nf.append(y)
        frontier = nf
    return target in S

def level_tiers(n, d, Bs):
    t = 4 * d; N = n + 4 * d
    if N % 2 == 0 or any(N % q == 0 for q in factors(d)): return None
    fs = factors(N)
    A = sigma(fs, t)
    res = {'A': (t - 1) in A, 'Gen': gen_has(fs, t, t - 1)}
    for B in Bs:
        small = [f for f in fs if f <= B]
        L = 1
        for f in fs:
            if f > B: L *= f
        S = sigma(small, t)
        if L > 1: S = S | {x * (L % t) % t for x in S}
        res['F%d' % B] = (t - 1) in S
    return res

def verify_b1(n, d):
    t = 4 * d; N = n + 4 * d
    divs = {1}
    for f in factors(N): divs |= {x * f for x in divs}
    for w in sorted(divs):
        if w % t == t - 1:
            c = (w + 1) // t; a = (c * n + 1) // w
            assert (c * n + 1) % w == 0
            x, y, z = a * d, a * c * d * n, c * d * n
            assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
            return True
    return False

def x2(n):
    # b=1 d-coordinate at d in {1,2,3,6}
    for d in (1, 2, 3, 6):
        r = level_tiers(n, d, [])
        if r and r['A']: return 'd%d' % d
    for c in (1, 2, 3, 6):
        N = c * n + 1
        while N % 2 == 0: N //= 2
        t = 4 * c
        if (t - 1) in sigma([f for f in factors(N) if (c % f) != 0 or f > c], t): return 'c%d' % c
    for N, nm in (((n + 3) // 4, 'II3'), ((3 * n + 1) // 4, 'I3')):
        fs = [f for f in factors(N) if f != 3]
        if any(f % 3 == 2 for f in fs): return nm  # a = f, b = 1: f ≡ −1 (3)
    return None

Bs = [int(b) for b in (sys.argv[3].split(",") if len(sys.argv) > 3 else ["30", "1000"])]
def run(ns, label):
    tiers = ['A', 'Gen'] + ['F%d' % B for B in Bs]
    cert = {k: 0 for k in tiers}; fails = {k: [] for k in tiers}; x2fail = []
    nver = 0
    for n in ns:
        got = {k: False for k in tiers}
        for d in range(1, D + 1):
            r = level_tiers(n, d, Bs)
            if r is None: continue
            for k in tiers:
                if r[k] and not got[k]:
                    got[k] = True
                    if k == 'A' and nver < 3000: assert verify_b1(n, d); nver += 1
            if all(got.values()): break
        for k in tiers:
            if got[k]: cert[k] += 1
            else: fails[k].append(n)
        if x2(n) is None: x2fail.append(n)
        # forced must imply actual
        for B in Bs: assert not (got['F%d' % B] and not got['A'])
    tot = len(ns)
    print(f"[{label}] n count {tot}, levels d <= {D}")
    for k in tiers:
        print(f"  {k:6s} certified {cert[k]:7d}  ({cert[k]/tot:.4f})  failures {len(fails[k])}  first {fails[k][:12]}")
    print(f"  X2     failures {len(x2fail)} ({len(x2fail)/tot:.4f}) first {x2fail[:12]} last {x2fail[-5:]}")
    return fails, x2fail

primes = [p for p in range(5, X + 1) if spf[p] == p and p % 4 == 1]
fails, x2f = run(primes, 'primes p≡1(4)')
squares = [m * m for m in range(3, int(X ** 0.5) + 1, 2)]
run(squares, 'odd squares (T1 control)')
for h in (193, 2521, 66529, 3361):
    if h <= X:
        print(h, {k: (h not in v) for k, v in fails.items()}, 'X2', h not in x2f)
