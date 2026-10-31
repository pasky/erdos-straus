"""z52b pass1 U05 Z3151 (min Omega(d) over C-form certificates d) and Z1075 (least winning C per p).
p≡1 (4), 5<=p<=6000, C<=150. For each p: least winning C (Z1075) and min Omega(d) over all winning (C,d) (Z3151),
where d | N=4Cp+1 and d ≡ -1 (mod 4C). Also the distribution of omega(d) of the minimal witness."""
import sys, math
from collections import Counter
sys.path.insert(0,'scripts')
def factor(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def divisors_with_omega(f):
    ds = [(1, 0)]
    for q, e in f.items():
        ds = [(d*q**k, o + (1 if k > 0 else 0)) for d, o in ds for k in range(e+1)]
    return ds
def primes_upto(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
ps = [p for p in primes_upto(6000) if p % 4 == 1 and p > 4]
least_C = {}; minOm = Counter(); worst = []
for p in ps:
    best_om = None; lc = None
    for C in range(1, 151):
        m = 4*C; f = factor(m*p+1)
        for d, Om in divisors_with_omega(f):
            if d % m == m-1:
                # Omega(d) counted with multiplicity
                g = factor(d); OmD = sum(g.values())
                if best_om is None or OmD < best_om: best_om = OmD
                if lc is None: lc = C
    least_C[p] = lc
    if best_om is not None: minOm[best_om] += 1
    if best_om is None or best_om >= 3: worst.append((p, best_om))
print("Z1075 least winning C (C<=150) for p≡1(4), p<=6000: max =", max(v for v in least_C.values() if v),
      "at p =", [p for p in least_C if least_C[p] == max(v for v in least_C.values() if v)])
print("  primes with no winner C<=150:", [p for p in least_C if least_C[p] is None])
print("  least winning C vs p (top 10 by C):", sorted(((least_C[p], p) for p in least_C if least_C[p]), reverse=True)[:10])
print("Z3151 min Omega(d) over all C<=150 certificates: distribution", dict(sorted(minOm.items())))
print("  primes where min Omega >= 3 or none (C<=150):", worst[:20], "count", len(worst))
