"""z52d avenue Q11 (Z1596): rich (★) level failures — p ≡ 1 (4) prime in [9·10⁴, 10⁵], C ≤ 200, ω(4Cp+1) ≥ 6, −1 ∉ D_C.
Is D_C (subset products of the prime factors of 4Cp+1 mod 4C, with multiplicity) a union of cosets of a non-trivial
subgroup (non-trivial stabiliser), and is the failure subgroup-type (−1 ∉ ⟨factors⟩)?
Run: timeout 60 python3 scripts/z52d_avenue_Q11_richfail.py"""
import numpy as np
from math import gcd
from collections import Counter
P0, P1, CM = 90000, 100000, 200
L = 4 * CM * P1 + 2
spf = np.zeros(L, dtype=np.int32)
for i in range(2, int(L ** .5) + 1):
    if spf[i] == 0:
        blk = spf[i * i::i]; blk[blk == 0] = i
def factor(n):
    f = {}
    while n > 1:
        q = int(spf[n]) or n
        f[q] = f.get(q, 0) + 1; n //= q
    return f
def subset_products(f, m):
    S = {1}
    for q, e in f.items():
        r = q % m; new = set(S); x = 1
        for _ in range(e):
            x = x * r % m; new |= {s * x % m for s in S}
        S = new
    return S
def gen_subgroup(rs, m):
    H = {1}; fr = [1]
    while fr:
        h = fr.pop()
        for r in rs:
            y = h * r % m
            if y not in H: H.add(y); fr.append(y)
    return H
ps = [p for p in range(P0 + 1, P1, 4) if spf[p] == 0]
res = Counter(); rich_total = 0
for p in ps:
    for C in range(1, CM + 1):
        m = 4 * C; f = factor(m * p + 1)
        if len(f) < 6: continue
        rich_total += 1
        D = subset_products(f, m)
        if (m - 1) in D: continue
        H = gen_subgroup([q % m for q in f], m)
        st = any({h * d % m for d in D} == D for h in range(2, m) if gcd(h, m) == 1)
        res[('subgroup' if (m - 1) not in H else 'poverty', 'stab' if st else 'nostab')] += 1
print(f'{len(ps)} primes, rich pairs (ω ≥ 6) {rich_total}, rich failures {sum(res.values())}:', dict(res))
